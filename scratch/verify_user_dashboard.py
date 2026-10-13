import re
import os
import subprocess

with open('user-dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

required_items = [
    # Module 1: Dashboard Overview
    "Active Event Projects", "Upcoming Events", "Pending Approvals", "Budget Summary", 
    "Vendor Booking Progress", "Recent Activity",
    
    # Module 2: My Profile
    "Personal Information", "Company Information", "Contact Details", "Profile Photo", "Change Password",
    
    # Module 3: My Events
    "Create New Event", "Submit Event Requirements", "Event Name & Type", "Event Date & Duration", 
    "Expected Attendee Count", "Preferred Location", "Event Objectives", "Special Requirements", 
    "Upload Event Documents", "Edit Event Requirements",
    
    # Module 4: Event Proposals
    "View Proposed Event Concepts", "Compare Proposal Options", "Review Service Inclusions", 
    "View Estimated Costs", "Request Proposal Changes", "Approve Proposal", "Proposal History",
    
    # Module 5: Venue Bookings
    "Suggested Venues", "Compare Venue Options", "Venue Images & Details", "Venue Availability", 
    "Booking Confirmation Status", "Venue Booking Documents",
    
    # Module 6: Vendor Bookings
    "Assigned Vendors", "Catering Booking Status", "Audio-Visual Booking Status", 
    "Decoration Booking Status", "Transport Booking Status", "Vendor Contact Details", 
    "Pending Vendor Confirmations", "Booking Issue Reports",
    
    # Module 7: Budget & Expenses
    "Approved Event Budget", "Venue Cost Breakdown", "Catering Cost Breakdown", 
    "Production & AV Costs", "Decoration & Branding Costs", "Vendor Service Charges", 
    "Additional Expenses", "Budget Utilization", "Change Request Estimates", "Download Budget Report",
    
    # Module 8: Event Timeline
    "Planning Milestones", "Upcoming Deadlines", "Task Completion Status", 
    "Client Action Items", "Event-Day Schedule", "Timeline Change Requests",
    
    # Module 9: Guest & Delegate Management
    "Upload Guest List", "Add & Edit Attendees", "Invitation Status", 
    "Registration Summary", "Attendance Summary", "Download Attendee List",
    
    # Module 10: Documents
    "Event Proposals", "Contracts & Agreements", "Approved Quotations", 
    "Vendor Agreements", "Event Schedules", "Invoices & Receipts", "Download Project Documents",
    
    # Module 11: Payments & Invoices
    "Advance Payments", "Pending Payments", "Completed Payments", 
    "Payment Transactions", "Invoice History", "Download Invoices", "Payment Confirmation",
    
    # Module 12: Communication
    "Messages to Event Manager", "Project Discussion Threads", "Meeting Requests", 
    "Meeting Notes", "Event Update Notifications", "Support Requests",
    
    # Module 13: Feedback & Reviews
    "Submit Event Feedback", "Rate Event Services", "Report Event Issues", 
    "Review Event Outcomes", "Download Final Event Report"
]

print("=== CHECKING REQUIRED CONTENT ITEMS ===")
missing = []
for item in required_items:
    # search case insensitive
    if item.lower() not in html.lower():
        missing.append(item)

if missing:
    print(f"FAILED: {len(missing)} items missing:")
    for m in missing:
        print(f"  - {m}")
else:
    print(f"SUCCESS: All {len(required_items)} sub-items found in user-dashboard.html!")

# Check 3D cube logo
print("\n=== CHECKING 3D CUBE LOGO ===")
has_cube = "logo-cube" in html and "logo-face" in html
print(f"3D Cube Logo Present: {has_cube}")

# Check custom scrollbar
print("\n=== CHECKING SLEEK SCROLLBAR ===")
has_scrollbar = "::-webkit-scrollbar" in html and "scrollbar-width" in html
print(f"Custom Sleek Scrollbar CSS Present: {has_scrollbar}")

# Check responsive topbar rules
print("\n=== CHECKING RESPONSIVE TOPBAR RULES ===")
has_media_1120 = "@media (max-width: 1120px)" in html or "@media (max-width: 1024px)" in html
print(f"Responsive Media Query Present: {has_media_1120}")

# Check JavaScript syntax
print("\n=== CHECKING JS SCRIPTS ===")
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} inline script blocks.")

for i, s in enumerate(scripts):
    test_file = f'scratch/test_user_dashboard_js_{i}.js'
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(s)
    res = subprocess.run(['node', '--check', test_file], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Script block {i}: Node syntax check PASSED.")
    else:
        print(f"Script block {i}: Node syntax check FAILED!\n{res.stderr}")
