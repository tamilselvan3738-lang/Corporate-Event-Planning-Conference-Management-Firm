# -*- coding: utf-8 -*-
"""
verify_admin_dashboard.py
Comprehensive verification script for admin-dashboard.html.
"""

import re, subprocess

def verify_dashboard():
    with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print("=== 1. TREE CONTENT & SUB-ITEMS AUDIT (88 ITEMS) ===")
    spec_tree = {
        "Dashboard Overview": [
            "Total Clients", "Active Event Projects", "Upcoming Events", "Pending Proposals",
            "Confirmed Vendor Bookings", "Revenue Summary", "Event Performance Metrics"
        ],
        "Client Management": [
            "Register Client", "View Client Accounts", "Edit Client Details", "Assign Event Manager",
            "Client Event History", "Activate / Deactivate Account"
        ],
        "Event Project Management": [
            "View All Event Requests", "Review Client Requirements", "Create Event Project",
            "Assign Project Team", "Update Project Status", "Manage Event Deadlines", "Archive Completed Projects"
        ],
        "Proposal Management": [
            "Create Event Proposal", "Configure Service Packages", "Prepare Cost Estimates",
            "Send Proposal to Client", "Review Client Feedback", "Track Proposal Approval"
        ],
        "Venue Management": [
            "Add Venue Details", "Edit Venue Information", "Manage Venue Availability",
            "Compare Venue Quotations", "Confirm Venue Reservations", "Track Venue Payments"
        ],
        "Vendor Management": [
            "Add Vendor", "Manage Vendor Profiles", "Categorize Vendor Services",
            "Request Vendor Quotations", "Assign Vendors to Events", "Confirm Vendor Bookings",
            "Track Booking Status", "Vendor Performance Reviews"
        ],
        "Budget Management": [
            "Set Project Budget", "Allocate Department Costs", "Record Project Expenses",
            "Review Additional Charges", "Monitor Budget Variance", "Approve Budget Changes",
            "Generate Financial Reports"
        ],
        "Schedule & Task Management": [
            "Create Project Timeline", "Assign Team Tasks", "Set Task Deadlines",
            "Monitor Task Progress", "Manage Event-Day Run Sheet", "Resolve Scheduling Conflicts"
        ],
        "Guest Registration Management": [
            "Manage Attendee Lists", "Configure Registration Forms", "Track Invitations",
            "Monitor Registration Counts", "Manage Check-In Records", "Export Attendee Data"
        ],
        "Contract & Document Management": [
            "Upload Client Contracts", "Manage Vendor Agreements", "Store Event Documents",
            "Track Document Approvals", "Manage Invoice Attachments"
        ],
        "Billing & Payment Management": [
            "Generate Client Invoices", "Track Advance Payments", "Monitor Outstanding Balances",
            "Record Vendor Payments", "Manage Refund Requests", "View Transaction History"
        ],
        "Communication Management": [
            "Client Messages", "Vendor Communications", "Send Project Updates",
            "Configure Email Notifications", "Manage Support Requests"
        ],
        "Feedback & Event Reports": [
            "Collect Client Reviews", "Evaluate Vendor Performance", "Generate Event Summary Reports",
            "Analyze Project Profitability", "Review Budget Performance", "Export Reports"
        ],
        "Website Content Management": [
            "Manage Home Page Sections", "Publish Portfolio Projects", "Update Service Information",
            "Manage Testimonials", "Publish Resource Articles", "Manage Contact Enquiries"
        ],
        "Logout": ["Logout"]
    }

    total_count = 0
    missing_items = []

    for category, sub_items in spec_tree.items():
        cat_present = category.lower() in html.lower()
        print(f"\n[MODULE] {category} -> {'PASS' if cat_present else 'FAIL'}")
        if not cat_present:
            missing_items.append(category)

        for item in sub_items:
            total_count += 1
            item_present = item.lower() in html.lower()
            if not item_present:
                missing_items.append(f"{category} -> {item}")

    print(f"\nTotal sub-items audited: {total_count}")
    if not missing_items:
        print("  [PASS] 100% OF ALL SPECIFIED TREE MODULES AND SUB-ITEMS ARE PRESENT!")
    else:
        print(f"  [FAIL] Missing {len(missing_items)} items: {missing_items}")
    assert len(missing_items) == 0, f"Missing items: {missing_items}"

    print("\n=== 2. MOBILE & TABLET LAYOUT REQUIREMENTS AUDIT ===")
    # Must have media query for <= 1120px covering all tablets and mobile devices
    assert "@media (max-width: 1120px)" in html, "Missing mobile/tab media query"
    print("  [PASS] Media query @media (max-width: 1120px) defined for mobile and tablet")

    # Check topbar-search, topbar-right, console-pill are hidden on mobile/tab
    assert ".console-pill {\n        display: none !important;\n      }" in html
    assert ".topbar-search {\n        display: none !important;\n      }" in html
    assert ".topbar-right {\n        display: none !important;\n      }" in html
    assert ".admin-sidebar {\n        display: none !important;\n      }" in html
    print("  [PASS] All non-logo/non-hamburger topbar items hidden on mobile/tab")

    # Check hamburger button visible on mobile/tab
    assert ".hamburger-btn {\n        display: flex !important;\n      }" in html
    print("  [PASS] Hamburger button display: flex !important on mobile/tab")


    # Check mobile drawer exists
    assert 'id="mobileDrawer"' in html
    assert 'id="drawerBackdrop"' in html
    print("  [PASS] Slide-out mobile drawer (#mobileDrawer) and backdrop defined")

    print("\n=== 3. COLOR THEME, LOGO & FONTS AUDIT ===")
    assert "Inter" in html
    assert "font-awesome" in html
    assert "logo-cube" in html
    assert "logo-3d" in html
    assert "body.rtl" in html
    assert "body.light" in html
    print("  [PASS] Inter font, Font Awesome 6, 3D rotating cube logo, RTL, and Light mode defined")

    print("\n=== 4. JAVASCRIPT SYNTAX CHECK (NODE --CHECK) ===")
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
    print(f"Total script blocks: {len(scripts)}")
    for idx, s in enumerate(scripts):
        fname = f'scratch/test_admin_js_{idx}.js'
        with open(fname, 'w', encoding='utf-8') as out:
            out.write(s)
        res = subprocess.run(['node', '--check', fname], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [PASS] Script block {idx}: Syntax valid")
        else:
            print(f"  [FAIL] Script block {idx}: Syntax error!\n{res.stderr}")
            assert False, "Syntax error in JavaScript"

    print("\n==========================================================")
    print(">>> ALL VERIFICATION CHECKS PASSED FOR ADMIN-DASHBOARD.HTML! <<<")
    print("==========================================================")

if __name__ == '__main__':
    verify_dashboard()
