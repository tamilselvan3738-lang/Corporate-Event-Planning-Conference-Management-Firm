# -*- coding: utf-8 -*-
"""
build_user_dashboard.py
Generates the complete user-dashboard.html for EventSphere Corporate Event Planning.
Guarantees:
- Same color theme (#070c18 / #0c1426 in dark, #f0f4fe in light, #2563eb sapphire blue accents)
- Same font styles (Inter + Font Awesome 6)
- Identical 3D rotating cube logo
- ALL 13 modules + Logout with ALL sub-items from user specification
- STRICT Mobile & Tablet layout: ON MOBILE & TAB VIEW (<= 1120px), ONLY logo on the left and hamburger menu on the right. ALL other things inside the hamburger menu!
- Custom sleek dark scrollbar (no ugly white scrollbar)
- Zero text wrapping on sidebar navigation and topbar buttons
"""

import os

def generate_user_dashboard():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EventSphere Client Portal | Executive Summit Dashboard</title>
  
  <!-- Inter Google Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700;14..32,800;14..32,900&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

  <style>
    /* ==========================================================================
       THEME VARIABLES & RESET (MATCHING ADMIN-DASHBOARD & INDEX.HTML)
       ========================================================================== */
    :root {
      --adm-bg: #070c18;
      --adm-surface: #0c1426;
      --adm-surface-card: #101c34;
      --adm-surface-card-hover: #142442;
      --adm-border: rgba(59, 130, 246, 0.16);
      --adm-border-subtle: rgba(255, 255, 255, 0.07);
      --adm-text-primary: #f8fafc;
      --adm-text-secondary: #94a3b8;
      --adm-text-muted: #64748b;
      --adm-primary-blue: #2563eb;
      --adm-primary-sky: #38bdf8;
      --adm-primary-emerald: #10b981;
      --adm-primary-amber: #f59e0b;
      --adm-primary-rose: #f43f5e;
      --adm-primary-purple: #8b5cf6;
      --adm-font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --sidebar-width: 340px;
      --topbar-height: 68px;
    }

    body.light {
      --adm-bg: #f0f4fe;
      --adm-surface: #ffffff;
      --adm-surface-card: #f8fafc;
      --adm-surface-card-hover: #f1f5f9;
      --adm-border: #e2e8f0;
      --adm-border-subtle: #cbd5e1;
      --adm-text-primary: #0f172a;
      --adm-text-secondary: #334155;
      --adm-text-muted: #64748b;
    }

    /* CUSTOM ULTRA-SLEEK DARK SCROLLBAR */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }

    ::-webkit-scrollbar-track {
      background: transparent;
    }

    ::-webkit-scrollbar-thumb {
      background: rgba(59, 130, 246, 0.25);
      border-radius: 9999px;
    }

    ::-webkit-scrollbar-thumb:hover {
      background: rgba(59, 130, 246, 0.5);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      scrollbar-width: thin;
      scrollbar-color: rgba(59, 130, 246, 0.25) transparent;
    }

    body {
      font-family: var(--adm-font);
      background-color: var(--adm-bg);
      color: var(--adm-text-secondary);
      min-height: 100vh;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* RTL Support */
    body.rtl {
      direction: rtl;
      text-align: right;
    }

    /* ==========================================================================
       3D LOGO STYLES (EXACTLY MATCHING NAVBAR & ADMIN CONSOLE)
       ========================================================================== */
    .logo-section {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      user-select: none;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .logo-3d {
      position: relative;
      width: 24px;
      height: 24px;
      perspective: 450px;
    }

    .logo-cube {
      width: 100%;
      height: 100%;
      position: relative;
      transform-style: preserve-3d;
      animation: rotateCube 14s infinite linear;
      transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    @keyframes rotateCube {
      0% { transform: rotateX(0deg) rotateY(0deg); }
      100% { transform: rotateX(360deg) rotateY(360deg); }
    }

    .logo-face {
      position: absolute;
      width: 24px;
      height: 24px;
      border-radius: 6px;
      background: linear-gradient(145deg, #1e3a8a, #3b82f6);
      box-shadow: 0 4px 8px rgba(0, 80, 200, 0.4), inset 0 1.5px 3px rgba(255,255,255,0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.65rem;
      color: white;
      border: 1px solid rgba(255,255,255,0.25);
    }

    .logo-face:nth-child(1) { transform: rotateY(0deg) translateZ(12px); }
    .logo-face:nth-child(2) { transform: rotateY(90deg) translateZ(12px); }
    .logo-face:nth-child(3) { transform: rotateY(180deg) translateZ(12px); }
    .logo-face:nth-child(4) { transform: rotateY(-90deg) translateZ(12px); }
    .logo-face:nth-child(5) { transform: rotateX(90deg) translateZ(12px); }
    .logo-face:nth-child(6) { transform: rotateX(-90deg) translateZ(12px); }

    .logo-text {
      font-size: 1.25rem;
      font-weight: 900;
      letter-spacing: -0.02em;
      color: var(--adm-text-primary);
      display: flex;
      align-items: center;
      gap: 0.15rem;
    }

    .logo-text span {
      background: linear-gradient(135deg, #60a5fa, #38bdf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .console-pill {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #34d399;
      margin-left: 0.5rem;
      white-space: nowrap;
      flex-shrink: 0;
    }

    body.rtl .console-pill {
      margin-left: 0;
      margin-right: 0.5rem;
    }

    /* ==========================================================================
       TOPBAR NAVIGATION BAR
       ========================================================================== */
    .admin-topbar {
      height: var(--topbar-height);
      background: var(--adm-surface);
      border-bottom: 1px solid var(--adm-border);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.25rem;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
      gap: 0.75rem;
      width: 100%;
      box-sizing: border-box;
      max-width: 100vw;
    }

    .topbar-left {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      flex-shrink: 0;
    }

    .topbar-search {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0 0.75rem;
      height: 38px;
      border-radius: 0.65rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      width: 200px;
      flex-shrink: 0;
      transition: all 0.25s ease;
    }

    .topbar-search:focus-within {
      border-color: var(--adm-primary-blue);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
    }

    .topbar-search input {
      background: transparent;
      border: none;
      outline: none;
      color: var(--adm-text-primary);
      font-size: 0.85rem;
      width: 100%;
      white-space: nowrap;
    }

    .topbar-search kbd {
      font-size: 0.68rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--adm-text-muted);
      border: 1px solid var(--adm-border-subtle);
      white-space: nowrap;
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-shrink: 0;
      white-space: nowrap;
    }

    .topbar-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      height: 38px;
      padding: 0 0.75rem;
      border-radius: 0.6rem;
      font-size: 0.82rem;
      font-weight: 600;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      text-decoration: none;
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s ease;
      box-sizing: border-box;
    }

    .topbar-btn:hover {
      background: var(--adm-surface-card-hover);
      color: var(--adm-text-primary);
      border-color: var(--adm-primary-blue);
    }

    .topbar-icon-btn {
      position: relative;
      width: 38px;
      height: 38px;
      border-radius: 0.6rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-secondary);
      cursor: pointer;
      font-size: 0.88rem;
      font-weight: 700;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s ease;
      box-sizing: border-box;
    }

    .topbar-icon-btn:hover {
      background: var(--adm-surface-card-hover);
      color: var(--adm-text-primary);
      border-color: var(--adm-primary-blue);
    }

    .notif-badge {
      position: absolute;
      top: -4px;
      right: -4px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #f43f5e;
      color: #fff;
      font-size: 0.65rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .user-profile-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      height: 40px;
      padding: 0 0.75rem;
      border-radius: 0.75rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
      box-sizing: border-box;
    }

    .avatar-ring {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, #2563eb, #38bdf8);
      color: #fff;
      font-weight: 800;
      font-size: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 10px rgba(37, 99, 235, 0.4);
      flex-shrink: 0;
    }

    .user-info {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
      white-space: nowrap;
    }

    .user-info strong {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--adm-text-primary);
      white-space: nowrap;
    }

    .user-info span {
      font-size: 0.68rem;
      color: var(--adm-text-muted);
      white-space: nowrap;
    }

    /* HAMBURGER BUTTON (Hidden on Desktop > 1120px, Visible on Mobile & Tablet) */
    .hamburger-btn {
      display: none;
      width: 44px;
      height: 44px;
      border-radius: 0.65rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-primary);
      font-size: 1.25rem;
      cursor: pointer;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .hamburger-btn:hover {
      background: var(--adm-primary-blue);
      color: #ffffff;
      border-color: var(--adm-primary-blue);
    }

    /* ==========================================================================
       DASHBOARD WRAPPER & SIDEBAR
       ========================================================================== */
    .dashboard-layout {
      display: flex;
      flex: 1;
      width: 100%;
      min-height: calc(100vh - var(--topbar-height));
    }

    .admin-sidebar {
      width: var(--sidebar-width);
      background: var(--adm-surface);
      border-right: 1px solid var(--adm-border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      height: calc(100vh - var(--topbar-height));
      position: sticky;
      top: var(--topbar-height);
      overflow-y: auto;
      overflow-x: hidden;
      padding: 1.25rem 0.75rem;
      box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
    }

    body.rtl .admin-sidebar {
      border-right: none;
      border-left: 1px solid var(--adm-border);
    }

    .sidebar-header-box {
      padding: 0.85rem 1rem;
      border-radius: 0.85rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      white-space: nowrap;
    }

    .node-status-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--adm-text-primary);
      display: flex;
      align-items: center;
      gap: 0.45rem;
      white-space: nowrap;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--adm-primary-emerald);
      box-shadow: 0 0 8px var(--adm-primary-emerald);
      flex-shrink: 0;
    }

    .node-subtext {
      font-size: 0.72rem;
      color: var(--adm-text-muted);
      margin-top: 0.2rem;
      white-space: nowrap;
    }

    .active-pill {
      font-size: 0.68rem;
      font-weight: 800;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
      white-space: nowrap;
      flex-shrink: 0;
    }

    .sidebar-nav-label {
      font-size: 0.7rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--adm-text-muted);
      padding: 0.5rem 0.65rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.35rem;
      white-space: nowrap;
    }

    .sidebar-menu-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .nav-module-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.62rem 0.85rem;
      border-radius: 0.75rem;
      color: var(--adm-text-secondary);
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid transparent;
      white-space: nowrap;
      gap: 0.5rem;
      height: 42px;
      box-sizing: border-box;
      width: 100%;
    }

    .nav-module-item:hover {
      background: var(--adm-surface-card);
      color: var(--adm-text-primary);
      border-color: var(--adm-border);
    }

    .nav-module-item.active {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(59, 130, 246, 0.1));
      color: #60a5fa;
      border-color: rgba(59, 130, 246, 0.35);
      font-weight: 700;
    }

    .item-left {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      white-space: nowrap;
      min-width: 0;
      flex: 1;
      overflow: hidden;
    }

    .item-left i {
      width: 20px;
      height: 20px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      flex-shrink: 0;
      text-align: center;
    }

    .item-left span {
      white-space: nowrap;
      font-size: 0.84rem;
      font-weight: 600;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .item-counter {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      background: var(--adm-surface-card);
      color: var(--adm-text-muted);
      border: 1px solid var(--adm-border-subtle);
      white-space: nowrap;
      flex-shrink: 0;
    }

    .nav-module-item.active .item-counter {
      background: #2563eb;
      color: #ffffff;
      border-color: transparent;
    }

    .logout-item {
      color: #f43f5e !important;
      margin-top: 0.75rem;
      border-top: 1px solid var(--adm-border-subtle);
      padding-top: 0.95rem;
    }

    .logout-item:hover {
      background: rgba(244, 63, 94, 0.1) !important;
      border-color: rgba(244, 63, 94, 0.25) !important;
    }

    /* ==========================================================================
       MAIN CONTENT PANEL
       ========================================================================== */
    .admin-main {
      flex: 1;
      min-width: 0;
      width: 100%;
      box-sizing: border-box;
      padding: 1.75rem 2rem 4rem 2rem;
      background: var(--adm-bg);
      overflow-y: auto;
      overflow-x: hidden;
    }

    .module-view {
      display: none;
      animation: fadeInView 0.35s ease;
    }

    .module-view.active {
      display: block;
    }

    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Module Header Bar */
    .module-header {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      margin-bottom: 2rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--adm-border);
    }

    .header-left-col h1 {
      font-size: 2.15rem;
      font-weight: 800;
      color: var(--adm-text-primary);
      letter-spacing: -0.02em;
      margin-bottom: 0.4rem;
    }

    .header-left-col p {
      font-size: 1rem;
      color: var(--adm-text-secondary);
      max-width: 720px;
      line-height: 1.5;
    }

    .header-actions-col {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.75rem;
    }

    .btn-action-primary {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      padding: 0.7rem 1.4rem;
      border-radius: 0.7rem;
      background: linear-gradient(135deg, #1e40af, #2563eb);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.9rem;
      border: 1px solid rgba(255, 255, 255, 0.15);
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
      transition: all 0.2s ease;
    }

    .btn-action-primary:hover {
      background: linear-gradient(135deg, #1d4ed8, #3b82f6);
      transform: translateY(-2px);
    }

    .btn-action-ghost {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      padding: 0.7rem 1.25rem;
      border-radius: 0.7rem;
      background: var(--adm-surface-card);
      color: var(--adm-text-primary);
      font-weight: 600;
      font-size: 0.9rem;
      border: 1px solid var(--adm-border);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-action-ghost:hover {
      background: var(--adm-surface-card-hover);
      border-color: var(--adm-primary-blue);
    }

    /* Sub-Features Navigation Chips */
    .subfeature-chips-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 2rem;
      padding: 0.6rem;
      border-radius: 0.85rem;
      background: var(--adm-surface);
      border: 1px solid var(--adm-border);
    }

    .subfeature-chip {
      padding: 0.45rem 1rem;
      border-radius: 0.6rem;
      font-size: 0.82rem;
      font-weight: 700;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border-subtle);
      color: var(--adm-text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .subfeature-chip:hover, .subfeature-chip.active {
      background: #2563eb;
      color: #ffffff;
      border-color: #2563eb;
    }

    /* ==========================================================================
       METRIC TELEMETRY CARDS (DASHBOARD OVERVIEW)
       ========================================================================== */
    .metrics-telemetry-grid {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: 1.25rem;
      margin-bottom: 2.25rem;
      width: 100%;
    }

    @media (min-width: 640px) {
      .metrics-telemetry-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1024px) {
      .metrics-telemetry-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    @media (min-width: 1300px) {
      .metrics-telemetry-grid {
        grid-template-columns: repeat(6, 1fr);
      }
    }

    .telemetry-card {
      padding: 1.5rem;
      border-radius: 1.15rem;
      background: var(--adm-surface);
      border: 1px solid var(--adm-border);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
      position: relative;
      overflow: hidden;
      transition: all 0.3s ease;
    }

    .telemetry-card:hover {
      transform: translateY(-3px);
      border-color: rgba(59, 130, 246, 0.35);
      box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.15);
    }

    .telemetry-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }

    .telemetry-label {
      font-size: 0.76rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--adm-text-muted);
    }

    .telemetry-icon-box {
      width: 38px;
      height: 38px;
      border-radius: 0.6rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      background: rgba(37, 99, 235, 0.12);
      color: #38bdf8;
    }

    .telemetry-val-large {
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--adm-text-primary);
      line-height: 1.1;
      margin-bottom: 0.75rem;
      letter-spacing: -0.02em;
    }

    .telemetry-trend-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .trend-pill {
      font-size: 0.75rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    .trend-pill.positive { color: #34d399; }
    .trend-pill.warning { color: #fbbf24; }
    .trend-pill.info { color: #60a5fa; }

    .sparkline-svg {
      width: 80px;
      height: 24px;
      overflow: visible;
    }

    /* ==========================================================================
       TWO-COLUMN TELEMETRY QUEUE & ACTIVITY FEED
       ========================================================================== */
    .overview-two-col {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.75rem;
      margin-bottom: 2.5rem;
    }

    @media (min-width: 1200px) {
      .overview-two-col {
        grid-template-columns: 1.4fr 1fr;
      }
    }

    .panel-card {
      padding: 1.75rem;
      border-radius: 1.15rem;
      background: var(--adm-surface);
      border: 1px solid var(--adm-border);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    }

    .panel-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid var(--adm-border-subtle);
    }

    .panel-header h3 {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--adm-text-primary);
    }

    .panel-action-link {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--adm-primary-blue);
      text-decoration: none;
      cursor: pointer;
    }

    /* Modern Table Styles */
    .data-table-wrapper {
      width: 100%;
      overflow-x: auto;
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.86rem;
    }

    body.rtl .data-table {
      text-align: right;
    }

    .data-table th {
      padding: 0.75rem 1rem;
      background: var(--adm-surface-card);
      color: var(--adm-text-muted);
      font-weight: 700;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--adm-border);
    }

    .data-table td {
      padding: 0.95rem 1rem;
      border-bottom: 1px solid var(--adm-border-subtle);
      color: var(--adm-text-secondary);
      vertical-align: middle;
    }

    .data-table tr:hover td {
      background: var(--adm-surface-card);
    }

    .status-badge {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }

    .badge-confirmed { background: rgba(16, 185, 129, 0.15); color: #34d399; }
    .badge-pending { background: rgba(245, 158, 11, 0.15); color: #fbbf24; }
    .badge-active { background: rgba(37, 99, 235, 0.15); color: #60a5fa; }
    .badge-draft { background: rgba(148, 163, 184, 0.15); color: #94a3b8; }
    .badge-danger { background: rgba(244, 63, 94, 0.15); color: #f43f5e; }

    /* Activity Feed Items */
    .activity-feed-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .activity-feed-item {
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      padding: 0.75rem;
      border-radius: 0.75rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border-subtle);
    }

    .activity-icon-badge {
      width: 32px;
      height: 32px;
      border-radius: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.82rem;
      flex-shrink: 0;
    }

    .activity-body {
      flex: 1;
    }

    .activity-text {
      font-size: 0.85rem;
      color: var(--adm-text-primary);
      line-height: 1.4;
    }

    .activity-time {
      font-size: 0.72rem;
      color: var(--adm-text-muted);
      margin-top: 0.25rem;
    }

    .table-btn {
      padding: 0.35rem 0.65rem;
      border-radius: 0.5rem;
      font-size: 0.78rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      transition: all 0.2s ease;
    }

    .table-btn-primary { background: #2563eb; color: #fff; }
    .table-btn-primary:hover { background: #1d4ed8; }
    .table-btn-ghost { background: var(--adm-surface-card); color: var(--adm-text-secondary); border: 1px solid var(--adm-border); }
    .table-btn-ghost:hover { background: var(--adm-surface-card-hover); color: var(--adm-text-primary); }

    /* ==========================================================================
       MODAL WINDOWS & FORMS
       ========================================================================== */
    .admin-modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      z-index: 500;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .admin-modal-overlay.open {
      display: flex;
    }

    .admin-modal-box {
      width: 100%;
      max-width: 650px;
      max-height: 90vh;
      overflow-y: auto;
      background: var(--adm-surface);
      border: 1px solid var(--adm-border);
      border-radius: 1.25rem;
      padding: 2rem;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.5);
      animation: modalScale 0.25s ease;
    }

    @keyframes modalScale {
      from { transform: scale(0.95); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .modal-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--adm-border-subtle);
    }

    .modal-header-row h3 {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--adm-text-primary);
    }

    .modal-close-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border-subtle);
      color: var(--adm-text-secondary);
      font-size: 1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .form-group {
      margin-bottom: 1.25rem;
    }

    .form-label {
      display: block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--adm-text-primary);
      margin-bottom: 0.45rem;
    }

    .form-control {
      width: 100%;
      padding: 0.75rem 1rem;
      border-radius: 0.65rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-primary);
      font-size: 0.9rem;
      outline: none;
    }

    .form-control:focus {
      border-color: var(--adm-primary-blue);
    }

    /* ==========================================================================
       MOBILE & TABLET DRAWER
       ========================================================================== */
    .mobile-drawer-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(4px);
      z-index: 998;
      display: none;
    }

    .mobile-drawer-backdrop.open {
      display: block;
    }

    .mobile-drawer {
      position: fixed;
      top: 0;
      right: 0;
      width: 340px;
      max-width: 85vw;
      height: 100vh;
      background: var(--adm-surface);
      border-left: 1px solid var(--adm-border);
      z-index: 999;
      display: flex;
      flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: -10px 0 35px rgba(0, 0, 0, 0.4);
      overflow-y: auto;
      padding: 1.5rem;
    }

    body.rtl .mobile-drawer {
      right: auto;
      left: 0;
      border-left: none;
      border-right: 1px solid var(--adm-border);
      transform: translateX(-100%);
    }

    .mobile-drawer.open {
      transform: translateX(0);
    }

    .drawer-top-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 1.25rem;
      margin-bottom: 1.25rem;
      border-bottom: 1px solid var(--adm-border-subtle);
    }

    .drawer-close-btn {
      width: 36px;
      height: 36px;
      border-radius: 0.6rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-primary);
      font-size: 1.1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .drawer-user-card {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      padding: 1rem;
      border-radius: 0.85rem;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      margin-bottom: 1.25rem;
    }

    .drawer-actions-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.5rem;
      margin-bottom: 1.5rem;
    }

    .drawer-action-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      padding: 0.65rem;
      border-radius: 0.65rem;
      font-size: 0.82rem;
      font-weight: 700;
      background: var(--adm-surface-card);
      border: 1px solid var(--adm-border);
      color: var(--adm-text-primary);
      text-decoration: none;
      cursor: pointer;
    }

    .drawer-action-btn:hover {
      background: var(--adm-surface-card-hover);
      border-color: var(--adm-primary-blue);
    }

    /* ==========================================================================
       MEDIA QUERIES: STRICT ADHERENCE TO MOBILE & TABLET REQUIREMENTS (<= 1120px)
       ========================================================================== */
    @media (max-width: 1120px) {
      /* TOPBAR: ONLY LOGO ON LEFT AND HAMBURGER ON RIGHT! */
      .console-pill {
        display: none !important;
      }

      .topbar-search {
        display: none !important;
      }

      .topbar-right {
        display: none !important;
      }

      .hamburger-btn {
        display: flex !important;
      }

      /* HIDE DESKTOP SIDEBAR COMPLETELY */
      .admin-sidebar {
        display: none !important;
      }

      /* MAIN CONTENT OCCUPIES FULL WIDTH */
      .admin-main {
        width: 100% !important;
        padding: 1.5rem 1rem 3rem 1rem !important;
      }

      .metrics-telemetry-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (min-width: 640px) and (max-width: 1120px) {
      .metrics-telemetry-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
  </style>
</head>
<body>

  <!-- ==========================================================================
       TOPBAR NAVIGATION
       ========================================================================== -->
  <header class="admin-topbar">
    <div class="topbar-left">
      <!-- LOGO (Always visible on left across Mobile, Tab, and Desktop) -->
      <a href="index.html" class="logo-section">
        <div class="logo-3d">
          <div class="logo-cube">
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
          </div>
        </div>
        <div class="logo-text">Event<span>Sphere</span></div>
        <span class="console-pill">CLIENT PORTAL</span>
      </a>

      <!-- Desktop Search (Hidden on Mobile & Tab <= 1120px) -->
      <div class="topbar-search">
        <i class="fas fa-search" style="color: var(--adm-text-muted);"></i>
        <input type="text" id="topbarSearchInput" placeholder="Quick Search...">
        <kbd>Ctrl K</kbd>
      </div>
    </div>

    <!-- Desktop Actions & Profile (Hidden on Mobile & Tab <= 1120px) -->
    <div class="topbar-right">
      <a href="index.html" class="topbar-btn" title="Back to Home Page">
        <i class="fas fa-home"></i> <span>Home</span>
      </a>
      <a href="admin-dashboard.html" class="topbar-btn" title="Switch to Admin Console">
        <i class="fas fa-shield-alt" style="color: #60a5fa;"></i> <span>Admin Console</span>
      </a>
      <button class="topbar-btn" id="refreshMetricsBtn" title="Refresh Live Metrics">
        <i class="fas fa-sync-alt"></i> <span>Refresh</span>
      </button>
      <button class="topbar-icon-btn" id="themeToggleBtn" title="Toggle Theme">
        <i class="fas fa-moon"></i>
      </button>
      <button class="topbar-icon-btn" id="rtlToggleBtn" title="Toggle RTL">
        RTL
      </button>
      <button class="topbar-icon-btn" id="notifBellBtn" title="Notifications">
        <i class="fas fa-bell"></i>
        <span class="notif-badge">3</span>
      </button>
      <div class="user-profile-badge" id="userProfileBadge" onclick="switchModule('my-profile')">
        <div class="avatar-ring">JS</div>
        <div class="user-info">
          <strong>Lord Julian Sterling</strong>
          <span>Chief Strategy Officer &bull; Client</span>
        </div>
      </div>
    </div>

    <!-- Hamburger Menu Button (ONLY visible on Mobile & Tab <= 1120px) -->
    <button class="hamburger-btn" id="hamburgerBtn" aria-label="Open Navigation Drawer">
      <i class="fas fa-bars"></i>
    </button>
  </header>

  <!-- ==========================================================================
       MOBILE & TABLET SLIDE-OUT DRAWER (CONTAINING ALL TOPBAR & SIDEBAR CONTENT)
       ========================================================================== -->
  <div class="mobile-drawer-backdrop" id="drawerBackdrop"></div>
  <aside class="mobile-drawer" id="mobileDrawer">
    <div class="drawer-top-row">
      <div class="logo-section">
        <div class="logo-3d">
          <div class="logo-cube">
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
            <div class="logo-face">&#10022;</div>
          </div>
        </div>
        <div class="logo-text">Event<span>Sphere</span></div>
      </div>
      <button class="drawer-close-btn" id="closeDrawerBtn">
        <i class="fas fa-times"></i>
      </button>
    </div>

    <!-- Drawer User Card -->
    <div class="drawer-user-card" onclick="switchModule('my-profile')" style="cursor: pointer;">
      <div class="avatar-ring">JS</div>
      <div class="user-info">
        <strong>Lord Julian Sterling</strong>
        <span>Chief Strategy Officer &bull; Client</span>
      </div>
    </div>

    <!-- Drawer Quick Actions -->
    <div class="drawer-actions-grid">
      <a href="index.html" class="drawer-action-btn">
        <i class="fas fa-home"></i> Home
      </a>
      <a href="admin-dashboard.html" class="drawer-action-btn">
        <i class="fas fa-shield-alt"></i> Admin
      </a>
      <button class="drawer-action-btn" id="drawerThemeBtn">
        <i class="fas fa-moon"></i> Theme
      </button>
      <button class="drawer-action-btn" id="drawerRtlBtn">
        <i class="fas fa-globe"></i> RTL
      </button>
    </div>

    <!-- Drawer Search Input -->
    <div style="margin-bottom: 1.25rem;">
      <div class="topbar-search" style="display: flex !important; width: 100%;">
        <i class="fas fa-search" style="color: var(--adm-text-muted);"></i>
        <input type="text" id="drawerSearchInput" placeholder="Search Portal...">
      </div>
    </div>

    <!-- Drawer Navigation Modules (All 13 Modules + Logout) -->
    <div class="sidebar-nav-label">
      <span>PORTAL NAVIGATION</span>
      <span>13 MODULES</span>
    </div>
    <ul class="sidebar-menu-list" id="drawerMenuList">
      <!-- Cloned via JS -->
    </ul>
  </aside>

  <!-- ==========================================================================
       DASHBOARD WRAPPER: DESKTOP SIDEBAR + MAIN CONTENT AREA
       ========================================================================== -->
  <div class="dashboard-layout">
    
    <!-- DESKTOP SIDEBAR (Visible > 1120px) -->
    <aside class="admin-sidebar" id="desktopSidebar">
      <div class="sidebar-header-box">
        <div>
          <div class="node-status-title">
            <span class="status-dot"></span>
            <span>CLIENT EXECUTIVE PORTAL</span>
          </div>
          <div class="node-subtext">Dedicated Director: Elena Rostova</div>
        </div>
        <span class="active-pill">TIER 1</span>
      </div>

      <div class="sidebar-nav-label">
        <span>PORTAL NAVIGATION</span>
        <span>13 MODULES</span>
      </div>

      <ul class="sidebar-menu-list" id="mainSidebarList">
        <!-- 1. Dashboard Overview -->
        <li>
          <a class="nav-module-item active" data-module="dashboard-overview">
            <span class="item-left">
              <i class="fas fa-chart-pie" style="color: #60a5fa;"></i>
              <span>Dashboard Overview</span>
            </span>
            <span class="item-counter" style="background:#2563eb; color:#fff;">LIVE</span>
          </a>
        </li>

        <!-- 2. My Profile -->
        <li>
          <a class="nav-module-item" data-module="my-profile">
            <span class="item-left">
              <i class="fas fa-user-circle" style="color: #38bdf8;"></i>
              <span>My Profile</span>
            </span>
            <span class="item-counter">Verified</span>
          </a>
        </li>

        <!-- 3. My Events -->
        <li>
          <a class="nav-module-item" data-module="my-events">
            <span class="item-left">
              <i class="fas fa-calendar-alt" style="color: #34d399;"></i>
              <span>My Events</span>
            </span>
            <span class="item-counter">3 Active</span>
          </a>
        </li>

        <!-- 4. Event Proposals -->
        <li>
          <a class="nav-module-item" data-module="event-proposals">
            <span class="item-left">
              <i class="fas fa-file-signature" style="color: #fbbf24;"></i>
              <span>Event Proposals</span>
            </span>
            <span class="item-counter">2 Pending</span>
          </a>
        </li>

        <!-- 5. Venue Bookings -->
        <li>
          <a class="nav-module-item" data-module="venue-bookings">
            <span class="item-left">
              <i class="fas fa-landmark" style="color: #a78bfa;"></i>
              <span>Venue Bookings</span>
            </span>
            <span class="item-counter">Confirmed</span>
          </a>
        </li>

        <!-- 6. Vendor Bookings -->
        <li>
          <a class="nav-module-item" data-module="vendor-bookings">
            <span class="item-left">
              <i class="fas fa-truck-loading" style="color: #f472b6;"></i>
              <span>Vendor Bookings</span>
            </span>
            <span class="item-counter">16/17</span>
          </a>
        </li>

        <!-- 7. Budget & Expenses -->
        <li>
          <a class="nav-module-item" data-module="budget-expenses">
            <span class="item-left">
              <i class="fas fa-wallet" style="color: #34d399;"></i>
              <span>Budget & Expenses</span>
            </span>
            <span class="item-counter">$685k</span>
          </a>
        </li>

        <!-- 8. Event Timeline -->
        <li>
          <a class="nav-module-item" data-module="event-timeline">
            <span class="item-left">
              <i class="fas fa-stream" style="color: #38bdf8;"></i>
              <span>Event Timeline</span>
            </span>
            <span class="item-counter">Milestones</span>
          </a>
        </li>

        <!-- 9. Guest & Delegate Management -->
        <li>
          <a class="nav-module-item" data-module="guest-management">
            <span class="item-left">
              <i class="fas fa-users" style="color: #fb923c;"></i>
              <span>Guest & Delegate Management</span>
            </span>
            <span class="item-counter">5,800 PAX</span>
          </a>
        </li>

        <!-- 10. Documents -->
        <li>
          <a class="nav-module-item" data-module="documents-vault">
            <span class="item-left">
              <i class="fas fa-folder-open" style="color: #60a5fa;"></i>
              <span>Documents</span>
            </span>
            <span class="item-counter">14 Files</span>
          </a>
        </li>

        <!-- 11. Payments & Invoices -->
        <li>
          <a class="nav-module-item" data-module="payments-invoices">
            <span class="item-left">
              <i class="fas fa-receipt" style="color: #4ade80;"></i>
              <span>Payments & Invoices</span>
            </span>
            <span class="item-counter">2 Paid</span>
          </a>
        </li>

        <!-- 12. Communication -->
        <li>
          <a class="nav-module-item" data-module="client-communication">
            <span class="item-left">
              <i class="fas fa-comments" style="color: #c084fc;"></i>
              <span>Communication</span>
            </span>
            <span class="item-counter">3 New</span>
          </a>
        </li>

        <!-- 13. Feedback & Reviews -->
        <li>
          <a class="nav-module-item" data-module="feedback-reviews">
            <span class="item-left">
              <i class="fas fa-star" style="color: #facc15;"></i>
              <span>Feedback & Reviews</span>
            </span>
            <span class="item-counter">Rate</span>
          </a>
        </li>

        <!-- 14. Logout -->
        <li>
          <a class="nav-module-item logout-item" id="sidebarLogoutBtn">
            <span class="item-left">
              <i class="fas fa-sign-out-alt"></i>
              <span>Logout</span>
            </span>
            <i class="fas fa-power-off"></i>
          </a>
        </li>
      </ul>
    </aside>

    <!-- ==========================================================================
         MAIN INTERACTIVE MODULE PANELS
         ========================================================================== -->
    <main class="admin-main">

      <!-- ======================================================================
           MODULE 1: DASHBOARD OVERVIEW (ACTIVE DEFAULT)
           ====================================================================== -->
      <section class="module-view active" id="view-dashboard-overview">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Executive Dashboard Overview</h1>
            <p>
              Welcome, Lord Julian Sterling. Track your corporate summit milestones, evaluate proposals, monitor vendor deployment, and inspect budget utilization.
            </p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="openModal('createEventModal')">
              <i class="fas fa-plus"></i> Submit Event Requirements
            </button>
            <button class="btn-action-ghost" onclick="switchModule('event-proposals')">
              <i class="fas fa-file-signature"></i> Review Proposals (2)
            </button>
            <button class="btn-action-ghost" onclick="alert('Downloading Executive Summit Briefing (PDF)...')">
              <i class="fas fa-download"></i> Executive Briefing
            </button>
          </div>
        </div>

        <!-- 6 Key Telemetry Cards matching user spec -->
        <div class="metrics-telemetry-grid">
          <!-- Card 1: Active Event Projects -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Active Event Projects</span>
              <div class="telemetry-icon-box" style="color: #38bdf8; background: rgba(56, 189, 248, 0.12);"><i class="fas fa-calendar-check"></i></div>
            </div>
            <div class="telemetry-val-large">3</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill positive"><i class="fas fa-check-circle"></i> On Schedule</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,18 Q20,12 40,15 T80,4" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>

          <!-- Card 2: Upcoming Events -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Upcoming Events</span>
              <div class="telemetry-icon-box" style="color: #a78bfa; background: rgba(167, 139, 250, 0.12);"><i class="fas fa-clock"></i></div>
            </div>
            <div class="telemetry-val-large">2</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill info">Nov 14 & Dec 02</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,20 Q20,14 45,16 T80,4" fill="none" stroke="#a78bfa" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>

          <!-- Card 3: Pending Approvals -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Pending Approvals</span>
              <div class="telemetry-icon-box" style="color: #fbbf24; background: rgba(245, 158, 11, 0.12);"><i class="fas fa-exclamation-circle"></i></div>
            </div>
            <div class="telemetry-val-large">4</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill warning"><i class="fas fa-circle" style="font-size:0.5rem;"></i> Action Required</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,15 Q25,8 50,18 T80,10" fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>

          <!-- Card 4: Budget Summary -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Budget Summary</span>
              <div class="telemetry-icon-box" style="color: #34d399; background: rgba(52, 211, 153, 0.12);"><i class="fas fa-wallet"></i></div>
            </div>
            <div class="telemetry-val-large">$685,000</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill positive">91.3% Committed</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,22 Q30,16 55,14 T80,4" fill="none" stroke="#34d399" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>

          <!-- Card 5: Vendor Booking Progress -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Vendor Booking Progress</span>
              <div class="telemetry-icon-box" style="color: #f472b6; background: rgba(244, 114, 182, 0.12);"><i class="fas fa-handshake"></i></div>
            </div>
            <div class="telemetry-val-large">94%</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill positive">16 of 17 Locked</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,18 Q30,12 50,15 T80,8" fill="none" stroke="#f472b6" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>

          <!-- Card 6: Registered Delegates -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Delegates Confirmed</span>
              <div class="telemetry-icon-box" style="color: #60a5fa; background: rgba(96, 165, 250, 0.12);"><i class="fas fa-id-badge"></i></div>
            </div>
            <div class="telemetry-val-large">4,210</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill positive">+18.4% MTD</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,20 Q20,15 40,10 T80,3" fill="none" stroke="#60a5fa" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>
        </div>

        <!-- Two-Column Overview: Action Queue + Recent Activity -->
        <div class="overview-two-col">
          <!-- Pending Approvals Table -->
          <div class="panel-card">
            <div class="panel-header">
              <h3><i class="fas fa-check-circle" style="color: #fbbf24;"></i> Client Action Items & Pending Approvals</h3>
              <a class="panel-action-link" onclick="switchModule('event-proposals')">View All (4) &rarr;</a>
            </div>
            <div class="data-table-wrapper">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>Decision Item</th>
                    <th>Project</th>
                    <th>Deadline</th>
                    <th>Status</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Sovereign 360&deg; LED Hologram Spec</strong></td>
                    <td>World FinTech Summit 2026</td>
                    <td>Tomorrow</td>
                    <td><span class="status-badge badge-pending">Sign-Off Required</span></td>
                    <td><button class="table-btn table-btn-primary" onclick="alert('Proposal Approved!')">Approve</button></td>
                  </tr>
                  <tr>
                    <td><strong>Michelin 7-Course Gala Banquet Menu</strong></td>
                    <td>World FinTech Summit 2026</td>
                    <td>Nov 05</td>
                    <td><span class="status-badge badge-pending">Menu Review</span></td>
                    <td><button class="table-btn table-btn-ghost" onclick="switchModule('vendor-bookings')">Review</button></td>
                  </tr>
                  <tr>
                    <td><strong>Zurich Alpine Glass Pavilion Contract</strong></td>
                    <td>Decarbonization Plenary</td>
                    <td>Nov 10</td>
                    <td><span class="status-badge badge-active">Deposit Ready</span></td>
                    <td><button class="table-btn table-btn-primary" onclick="switchModule('payments-invoices')">Settle</button></td>
                  </tr>
                  <tr>
                    <td><strong>Biometric VIP Escort Route Protocol</strong></td>
                    <td>World FinTech Summit 2026</td>
                    <td>Nov 12</td>
                    <td><span class="status-badge badge-draft">Draft Available</span></td>
                    <td><button class="table-btn table-btn-ghost" onclick="switchModule('documents-vault')">Inspect</button></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Recent Activity Feed -->
          <div class="panel-card">
            <div class="panel-header">
              <h3><i class="fas fa-history" style="color: #38bdf8;"></i> Recent Activity Stream</h3>
              <span class="status-badge badge-confirmed">Live Synchronized</span>
            </div>
            <div class="activity-feed-list">
              <div class="activity-feed-item">
                <div class="activity-icon-badge" style="background: rgba(37,99,235,0.15); color: #38bdf8;">
                  <i class="fas fa-file-contract"></i>
                </div>
                <div class="activity-body">
                  <div class="activity-text"><strong>Elena Rostova</strong> published revised Stage Architecture Proposal v2.4.</div>
                  <div class="activity-time">15 minutes ago &bull; Event Proposals</div>
                </div>
              </div>
              <div class="activity-feed-item">
                <div class="activity-icon-badge" style="background: rgba(16,185,129,0.15); color: #34d399;">
                  <i class="fas fa-check-double"></i>
                </div>
                <div class="activity-body">
                  <div class="activity-text">Venue deposit of <strong>$180,000</strong> confirmed by Geneva Convention Hall.</div>
                  <div class="activity-time">2 hours ago &bull; Venue Bookings</div>
                </div>
              </div>
              <div class="activity-feed-item">
                <div class="activity-icon-badge" style="background: rgba(245,158,11,0.15); color: #fbbf24;">
                  <i class="fas fa-users"></i>
                </div>
                <div class="activity-body">
                  <div class="activity-text"><strong>120 New VIP Registrations</strong> added to Guest & Delegate list.</div>
                  <div class="activity-time">5 hours ago &bull; Delegate Concierge</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 2: MY PROFILE
           ====================================================================== -->
      <section class="module-view" id="view-my-profile">
        <div class="module-header">
          <div class="header-left-col">
            <h1>My Profile & Executive Credentials</h1>
            <p>Manage your executive profile, corporate credentials, protocol contact details, and account security.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Profile details updated successfully!')"><i class="fas fa-save"></i> Save Changes</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Personal Information</button>
          <button class="subfeature-chip">Company Information</button>
          <button class="subfeature-chip">Contact Details</button>
          <button class="subfeature-chip">Profile Photo</button>
          <button class="subfeature-chip">Change Password</button>
        </div>

        <div class="panel-card" style="max-width: 900px;">
          <!-- Profile Card Header -->
          <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--adm-border-subtle);">
            <div class="avatar-ring" style="width: 72px; height: 72px; font-size: 1.8rem;">JS</div>
            <div>
              <h3 style="font-size: 1.4rem; color: var(--adm-text-primary);">Lord Julian Sterling</h3>
              <p style="font-size: 0.9rem; color: var(--adm-text-secondary);">Chief Strategy Officer &bull; Goldman Sovereign Capital</p>
              <span class="status-badge badge-confirmed" style="margin-top: 0.4rem;"><i class="fas fa-crown"></i> Tier-1 Sovereign Enterprise Client</span>
            </div>
            <button class="btn-action-ghost" style="margin-left: auto;" onclick="alert('Open Photo Uploader...')"><i class="fas fa-camera"></i> Change Photo</button>
          </div>

          <!-- Personal Information Form -->
          <form onsubmit="event.preventDefault(); alert('Profile information saved!');">
            <h4 style="font-size: 1.1rem; color: var(--adm-text-primary); margin-bottom: 1rem;"><i class="fas fa-user-edit" style="color: #2563eb;"></i> Personal Information</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
              <div class="form-group">
                <label class="form-label">First Name *</label>
                <input type="text" class="form-control" value="Julian">
              </div>
              <div class="form-group">
                <label class="form-label">Last Name *</label>
                <input type="text" class="form-control" value="Sterling">
              </div>
            </div>

            <h4 style="font-size: 1.1rem; color: var(--adm-text-primary); margin-bottom: 1rem;"><i class="fas fa-building" style="color: #38bdf8;"></i> Company Information</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
              <div class="form-group">
                <label class="form-label">Company / Corporation *</label>
                <input type="text" class="form-control" value="Goldman Sovereign Capital">
              </div>
              <div class="form-group">
                <label class="form-label">Corporate Title *</label>
                <input type="text" class="form-control" value="Chief Strategy Officer">
              </div>
            </div>

            <h4 style="font-size: 1.1rem; color: var(--adm-text-primary); margin-bottom: 1rem;"><i class="fas fa-address-book" style="color: #10b981;"></i> Contact Details</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
              <div class="form-group">
                <label class="form-label">Institutional Business Email *</label>
                <input type="email" class="form-control" value="j.sterling@goldman-sovereign.ch">
              </div>
              <div class="form-group">
                <label class="form-label">Direct Secure Telephony</label>
                <input type="text" class="form-control" value="+41 22 819 9000">
              </div>
            </div>

            <h4 style="font-size: 1.1rem; color: var(--adm-text-primary); margin-bottom: 1rem;"><i class="fas fa-key" style="color: #f59e0b;"></i> Change Password</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
              <div class="form-group">
                <label class="form-label">Current Password</label>
                <input type="password" class="form-control" placeholder="••••••••••••">
              </div>
              <div class="form-group">
                <label class="form-label">New Password</label>
                <input type="password" class="form-control" placeholder="Enter new password">
              </div>
            </div>

            <button type="submit" class="btn-action-primary"><i class="fas fa-check"></i> Update Profile Credentials</button>
          </form>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 3: MY EVENTS
           ====================================================================== -->
      <section class="module-view" id="view-my-events">
        <div class="module-header">
          <div class="header-left-col">
            <h1>My Events & Requirements</h1>
            <p>Track your active corporate summits, submit new requirements, upload briefings, and coordinate event parameters.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="openModal('createEventModal')"><i class="fas fa-plus"></i> Create New Event</button>
            <button class="btn-action-ghost" onclick="openModal('createEventModal')"><i class="fas fa-file-upload"></i> Submit Requirements</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">My Events Overview</button>
          <button class="subfeature-chip" onclick="openModal('createEventModal')">Create New Event</button>
          <button class="subfeature-chip" onclick="openModal('createEventModal')">Submit Event Requirements</button>
          <button class="subfeature-chip">Event Name & Type</button>
          <button class="subfeature-chip">Event Date & Duration</button>
          <button class="subfeature-chip">Expected Attendee Count</button>
          <button class="subfeature-chip">Preferred Location</button>
          <button class="subfeature-chip">Event Objectives</button>
          <button class="subfeature-chip">Special Requirements</button>
          <button class="subfeature-chip">Upload Event Documents</button>
          <button class="subfeature-chip">Edit Event Requirements</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Event Name & Type</th>
                  <th>Date & Duration</th>
                  <th>Expected Attendees</th>
                  <th>Preferred Location</th>
                  <th>Strategic Objectives</th>
                  <th>Status & Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>World FinTech Sovereign Summit</strong><br><span style="font-size:0.75rem; color:var(--adm-text-muted);">Giga-Plenary & Treaty Forum</span></td>
                  <td>Nov 14 - 17, 2026 (4 Days)</td>
                  <td>5,800 Delegates</td>
                  <td>Geneva, Switzerland</td>
                  <td>$4B+ Liquidity & Bilateral Banking Accords</td>
                  <td>
                    <span class="status-badge badge-confirmed">Active Production</span>
                    <button class="table-btn table-btn-primary" style="margin-left:0.5rem;" onclick="openModal('createEventModal')">Edit Requirements</button>
                  </td>
                </tr>
                <tr>
                  <td><strong>Global Decarbonization Accord</strong><br><span style="font-size:0.75rem; color:var(--adm-text-muted);">Ministerial Clean Energy Assembly</span></td>
                  <td>Dec 02 - 04, 2026 (3 Days)</td>
                  <td>1,400 Delegates</td>
                  <td>Zurich Alpine Pavilion</td>
                  <td>ISO-20121 Zero-Carbon Treaty Execution</td>
                  <td>
                    <span class="status-badge badge-active">Venue Confirmed</span>
                    <button class="table-btn table-btn-primary" style="margin-left:0.5rem;" onclick="openModal('createEventModal')">Edit Requirements</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 4: EVENT PROPOSALS
           ====================================================================== -->
      <section class="module-view" id="view-event-proposals">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Event Proposals & Concept Options</h1>
            <p>Review custom production concepts, compare proposal options, inspect estimated costs, and approve packages.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Proposal approved and signed off!')"><i class="fas fa-check"></i> Approve Proposal</button>
            <button class="btn-action-ghost" onclick="alert('Requesting revisions from Event Director...')"><i class="fas fa-edit"></i> Request Proposal Changes</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">View Proposed Event Concepts</button>
          <button class="subfeature-chip">Compare Proposal Options</button>
          <button class="subfeature-chip">Review Service Inclusions</button>
          <button class="subfeature-chip">View Estimated Costs</button>
          <button class="subfeature-chip" onclick="alert('Requesting changes...')">Request Proposal Changes</button>
          <button class="subfeature-chip" onclick="alert('Proposal approved!')">Approve Proposal</button>
          <button class="subfeature-chip">Proposal History</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Concept Title</th>
                  <th>Proposal Option Tier</th>
                  <th>Key Service Inclusions</th>
                  <th>Estimated Costs</th>
                  <th>Approval Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Option A: Sovereign 360&deg; LED Holographic Plenary</strong></td>
                  <td>Tier 1 Sovereign Flagship</td>
                  <td>Panoramic 360&deg; microLED, 432Hz psychoacoustic tuning, 16 translation booths</td>
                  <td><strong>$485,000</strong></td>
                  <td><span class="status-badge badge-confirmed">Ready for Approval</span></td>
                  <td><button class="table-btn table-btn-primary" onclick="alert('Option A Approved!')">Approve Proposal</button></td>
                </tr>
                <tr>
                  <td><strong>Option B: Executive Dual-Stage Panoramic Hybrid</strong></td>
                  <td>Tier 2 Executive Standard</td>
                  <td>Dual curved LED displays, sub-20ms telepresence, 8 translation booths</td>
                  <td><strong>$380,000</strong></td>
                  <td><span class="status-badge badge-draft">Alternate Option</span></td>
                  <td><button class="table-btn table-btn-ghost">Compare</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 5: VENUE BOOKINGS
           ====================================================================== -->
      <section class="module-view" id="view-venue-bookings">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Venue Bookings & Availability</h1>
            <p>Curated luxury convention complexes, space availability calendars, quotation comparisons, and confirmation records.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Downloading Venue Confirmation Documents...')"><i class="fas fa-file-download"></i> Venue Booking Documents</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Suggested Venues</button>
          <button class="subfeature-chip">Compare Venue Options</button>
          <button class="subfeature-chip">Venue Images & Details</button>
          <button class="subfeature-chip">Venue Availability</button>
          <button class="subfeature-chip">Booking Confirmation Status</button>
          <button class="subfeature-chip">Venue Booking Documents</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Suggested Venue</th>
                  <th>Location & Details</th>
                  <th>Availability Calendar</th>
                  <th>Booking Confirmation Status</th>
                  <th>Contract Documents</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Geneva Grand Amphitheatre</strong></td>
                  <td>Geneva, Switzerland &bull; 6,500 PAX &bull; -52dB Isolation</td>
                  <td><span class="status-badge badge-confirmed">Locked (Nov 14-17)</span></td>
                  <td><span class="status-badge badge-confirmed"><i class="fas fa-check-circle"></i> Confirmed & Paid</span></td>
                  <td><button class="table-btn table-btn-primary">Download Lease</button></td>
                </tr>
                <tr>
                  <td><strong>Zurich Alpine Glass Pavilion</strong></td>
                  <td>Zurich, Switzerland &bull; 2,200 PAX &bull; Biophilic Green</td>
                  <td><span class="status-badge badge-active">Option Held (Dec 02-04)</span></td>
                  <td><span class="status-badge badge-pending">Deposit Scheduled</span></td>
                  <td><button class="table-btn table-btn-ghost">View Hold Cert</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 6: VENDOR BOOKINGS
           ====================================================================== -->
      <section class="module-view" id="view-vendor-bookings">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Vendor Bookings & Supplier Deployment</h1>
            <p>Track assigned suppliers across catering, audio-visual, stage production, transport, and report booking issues.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Opening Issue Report Dialog...')"><i class="fas fa-exclamation-triangle"></i> Booking Issue Reports</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Assigned Vendors</button>
          <button class="subfeature-chip">Catering Booking Status</button>
          <button class="subfeature-chip">Audio-Visual Booking Status</button>
          <button class="subfeature-chip">Decoration Booking Status</button>
          <button class="subfeature-chip">Transport Booking Status</button>
          <button class="subfeature-chip">Vendor Contact Details</button>
          <button class="subfeature-chip">Pending Vendor Confirmations</button>
          <button class="subfeature-chip" onclick="alert('Report booking issue...')">Booking Issue Reports</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Category</th>
                  <th>Assigned Vendor Partner</th>
                  <th>Booking Confirmation Status</th>
                  <th>Vendor Contact Details</th>
                  <th>SLA Rating</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><i class="fas fa-video text-sky-400"></i> Audio-Visual</td>
                  <td><strong>Apex Holographic AV Solutions</strong></td>
                  <td><span class="status-badge badge-confirmed">Confirmed Booking</span></td>
                  <td>apex-dispatch@event-av.ch &bull; +41 22 990 1200</td>
                  <td><span style="color:#fbbf24;">&#9733;&#9733;&#9733;&#9733;&#9733; 4.95</span></td>
                </tr>
                <tr>
                  <td><i class="fas fa-utensils text-amber-400"></i> Catering</td>
                  <td><strong>Michelin Executive Catering Guild</strong></td>
                  <td><span class="status-badge badge-confirmed">Confirmed Booking</span></td>
                  <td>guild@michelin-corp.ch &bull; +41 22 990 3400</td>
                  <td><span style="color:#fbbf24;">&#9733;&#9733;&#9733;&#9733;&#9734; 4.88</span></td>
                </tr>
                <tr>
                  <td><i class="fas fa-palette text-purple-400"></i> Decoration</td>
                  <td><strong>Sovereign Scenic & Stage Forge</strong></td>
                  <td><span class="status-badge badge-confirmed">Confirmed Booking</span></td>
                  <td>forge@sovereign-stages.com &bull; +44 20 7946 0991</td>
                  <td><span style="color:#fbbf24;">&#9733;&#9733;&#9733;&#9733;&#9733; 4.92</span></td>
                </tr>
                <tr>
                  <td><i class="fas fa-car-side text-emerald-400"></i> Transport</td>
                  <td><strong>Swiss Royal Armored Logistics</strong></td>
                  <td><span class="status-badge badge-pending">Pending Final Confirmation</span></td>
                  <td>armored-vip@swisslogistics.ch &bull; +41 22 990 8800</td>
                  <td><span style="color:#fbbf24;">&#9733;&#9733;&#9733;&#9733;&#9734; 4.85</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 7: BUDGET & EXPENSES
           ====================================================================== -->
      <section class="module-view" id="view-budget-expenses">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Budget & Expenses Telemetry</h1>
            <p>Itemized departmental costs, approved event budgets, live budget utilization, change request estimates, and audit reports.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Downloading Itemized Budget Report (PDF)...')"><i class="fas fa-download"></i> Download Budget Report</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Approved Event Budget</button>
          <button class="subfeature-chip">Venue Cost Breakdown</button>
          <button class="subfeature-chip">Catering Cost Breakdown</button>
          <button class="subfeature-chip">Production & AV Costs</button>
          <button class="subfeature-chip">Decoration & Branding Costs</button>
          <button class="subfeature-chip">Vendor Service Charges</button>
          <button class="subfeature-chip">Additional Expenses</button>
          <button class="subfeature-chip">Budget Utilization</button>
          <button class="subfeature-chip">Change Request Estimates</button>
          <button class="subfeature-chip" onclick="alert('Downloading report...')">Download Budget Report</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Cost Allocation Department</th>
                  <th>Approved Event Budget</th>
                  <th>Committed Spend</th>
                  <th>Budget Utilization</th>
                  <th>Change Request Estimates</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Venue Rental & Space Licensing</strong></td>
                  <td>$180,000</td>
                  <td>$180,000</td>
                  <td><span class="status-badge badge-confirmed">100% Utilized</span></td>
                  <td>$0 (Fixed Contract)</td>
                </tr>
                <tr>
                  <td><strong>Audio-Visual & 8K Hologram Production</strong></td>
                  <td>$220,000</td>
                  <td>$210,000</td>
                  <td><span class="status-badge badge-confirmed">95.5% Utilized</span></td>
                  <td>+$10,000 Optional 3D Stream</td>
                </tr>
                <tr>
                  <td><strong>Catering & Delegate Hospitality</strong></td>
                  <td>$140,000</td>
                  <td>$128,000</td>
                  <td><span class="status-badge badge-confirmed">91.4% Utilized</span></td>
                  <td>+$4,500 VIP Sommelier Addon</td>
                </tr>
                <tr>
                  <td><strong>Decoration & Stage Branding Architecture</strong></td>
                  <td>$85,000</td>
                  <td>$78,500</td>
                  <td><span class="status-badge badge-confirmed">92.4% Utilized</span></td>
                  <td>$0 (Included)</td>
                </tr>
                <tr>
                  <td><strong>Transport & Biometric Security Coordination</strong></td>
                  <td>$75,000</td>
                  <td>$68,500</td>
                  <td><span class="status-badge badge-confirmed">91.3% Utilized</span></td>
                  <td>$0 (Included)</td>
                </tr>
                <tr>
                  <td><strong>Contingency Reserve & Additional Expenses</strong></td>
                  <td>$50,000</td>
                  <td>$20,000</td>
                  <td><span class="status-badge badge-active">40.0% Utilized</span></td>
                  <td>$30,000 Reserve Intact</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 8: EVENT TIMELINE
           ====================================================================== -->
      <section class="module-view" id="view-event-timeline">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Event Timeline & Milestone Schedule</h1>
            <p>Planning milestones, upcoming deadlines, task completion tracking, client action items, and day-of schedules.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Opening Timeline Change Request...')"><i class="fas fa-calendar-check"></i> Timeline Change Requests</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Planning Milestones</button>
          <button class="subfeature-chip">Upcoming Deadlines</button>
          <button class="subfeature-chip">Task Completion Status</button>
          <button class="subfeature-chip">Client Action Items</button>
          <button class="subfeature-chip">Event-Day Schedule</button>
          <button class="subfeature-chip" onclick="alert('Submit Change Request...')">Timeline Change Requests</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Milestone Timeline Phase</th>
                  <th>Key Planning Deliverable</th>
                  <th>Upcoming Deadlines</th>
                  <th>Task Completion Status</th>
                  <th>Client Action Items</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Phase 1: Discovery & Concept</strong></td>
                  <td>Strategic Objectives & Capacity Scoping</td>
                  <td>Completed</td>
                  <td><span class="status-badge badge-confirmed">100% Completed</span></td>
                  <td>None (Signed off)</td>
                </tr>
                <tr>
                  <td><strong>Phase 2: Venue & AV Architecture</strong></td>
                  <td>Amphitheatre Acoustics & LED Trusses</td>
                  <td>Oct 20, 2026</td>
                  <td><span class="status-badge badge-confirmed">100% Completed</span></td>
                  <td>None (Signed off)</td>
                </tr>
                <tr>
                  <td><strong>Phase 3: VIP Protocol & Delegate Accords</strong></td>
                  <td>Security Routes & Invitation Dispatches</td>
                  <td>Nov 01, 2026</td>
                  <td><span class="status-badge badge-active">85% In Progress</span></td>
                  <td><button class="table-btn table-btn-primary">Approve Seating Chart</button></td>
                </tr>
                <tr>
                  <td><strong>Phase 4: Event-Day Live Execution</strong></td>
                  <td>Full Plenary Rehearsal & Live Transmission</td>
                  <td>Nov 14, 2026</td>
                  <td><span class="status-badge badge-draft">Scheduled</span></td>
                  <td>Review Run Sheet</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 9: GUEST & DELEGATE MANAGEMENT
           ====================================================================== -->
      <section class="module-view" id="view-guest-management">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Guest & Delegate Management</h1>
            <p>Upload guest lists, manage VIP invitations, review registration and attendance telemetry, and export rosters.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Select CSV/Excel Guest List to Upload...')"><i class="fas fa-file-upload"></i> Upload Guest List</button>
            <button class="btn-action-ghost" onclick="alert('Downloading Attendee List (CSV)...')"><i class="fas fa-download"></i> Download Attendee List</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Upload Guest List</button>
          <button class="subfeature-chip">Add & Edit Attendees</button>
          <button class="subfeature-chip">Invitation Status</button>
          <button class="subfeature-chip">Registration Summary</button>
          <button class="subfeature-chip">Attendance Summary</button>
          <button class="subfeature-chip" onclick="alert('Downloading...')">Download Attendee List</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Delegate Name & Title</th>
                  <th>Organization / Institution</th>
                  <th>Invitation Status</th>
                  <th>Registration Summary</th>
                  <th>Attendance Summary</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Sir Arthur Kensington</strong> (Governor)</td>
                  <td>Bank of England / FCA</td>
                  <td><span class="status-badge badge-confirmed">Invitation Confirmed</span></td>
                  <td>VIP Sovereign Pass</td>
                  <td><span class="status-badge badge-confirmed">Confirmed In-Person</span></td>
                  <td><button class="table-btn table-btn-primary">Edit Attendee</button></td>
                </tr>
                <tr>
                  <td><strong>Hon. Beatrice Dupont</strong> (Ambassador)</td>
                  <td>Swiss Federal Council</td>
                  <td><span class="status-badge badge-confirmed">Invitation Confirmed</span></td>
                  <td>Diplomatic Protocol</td>
                  <td><span class="status-badge badge-confirmed">Confirmed In-Person</span></td>
                  <td><button class="table-btn table-btn-primary">Edit Attendee</button></td>
                </tr>
                <tr>
                  <td><strong>Dr. Aris Thorne</strong> (Managing Director)</td>
                  <td>Nordic Clean Tech Capital</td>
                  <td><span class="status-badge badge-pending">Invitation Pending</span></td>
                  <td>Executive Plenary</td>
                  <td><span class="status-badge badge-draft">Awaiting RSVP</span></td>
                  <td><button class="table-btn table-btn-ghost">Resend Invite</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 10: DOCUMENTS
           ====================================================================== -->
      <section class="module-view" id="view-documents-vault">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Document Vault & Legal Repository</h1>
            <p>Access signed proposals, contracts, approved quotations, vendor agreements, schedules, and invoices.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Downloading Complete Project Document Archive (ZIP)...')"><i class="fas fa-download"></i> Download Project Documents</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Event Proposals</button>
          <button class="subfeature-chip">Contracts & Agreements</button>
          <button class="subfeature-chip">Approved Quotations</button>
          <button class="subfeature-chip">Vendor Agreements</button>
          <button class="subfeature-chip">Event Schedules</button>
          <button class="subfeature-chip">Invoices & Receipts</button>
          <button class="subfeature-chip" onclick="alert('Downloading...')">Download Project Documents</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Document Title</th>
                  <th>Category</th>
                  <th>Execution Date</th>
                  <th>Security Verification</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>MSA_GoldmanSovereign_EventSphere_Final.pdf</strong></td>
                  <td>Contracts & Agreements</td>
                  <td>Oct 08, 2026</td>
                  <td><span class="status-badge badge-confirmed">Dual-Signed (DocuSign)</span></td>
                  <td><button class="table-btn table-btn-primary">Download</button></td>
                </tr>
                <tr>
                  <td><strong>Approved_Quotation_GenevaAmphitheatre_2026.pdf</strong></td>
                  <td>Approved Quotations</td>
                  <td>Oct 10, 2026</td>
                  <td><span class="status-badge badge-confirmed">Verified Lease</span></td>
                  <td><button class="table-btn table-btn-primary">Download</button></td>
                </tr>
                <tr>
                  <td><strong>MinuteByMinute_EventSchedule_WorldFinTech.pdf</strong></td>
                  <td>Event Schedules</td>
                  <td>Oct 12, 2026</td>
                  <td><span class="status-badge badge-active">Active Draft v4.2</span></td>
                  <td><button class="table-btn table-btn-primary">Download</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 11: PAYMENTS & INVOICES
           ====================================================================== -->
      <section class="module-view" id="view-payments-invoices">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Payments & Invoices Management</h1>
            <p>Track advance payments, pending installments, completed transfers, receipt records, and settlement confirmations.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Downloading All Invoice Receipts (PDF)...')"><i class="fas fa-file-download"></i> Download Invoices</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Advance Payments</button>
          <button class="subfeature-chip">Pending Payments</button>
          <button class="subfeature-chip">Completed Payments</button>
          <button class="subfeature-chip">Payment Transactions</button>
          <button class="subfeature-chip">Invoice History</button>
          <button class="subfeature-chip" onclick="alert('Downloading...')">Download Invoices</button>
          <button class="subfeature-chip">Payment Confirmation</button>
        </div>

        <div class="panel-card">
          <div class="data-table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Invoice Reference</th>
                  <th>Payment Milestone Description</th>
                  <th>Amount</th>
                  <th>Status & Confirmation</th>
                  <th>Invoice History / Download</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>INV-2026-4401</strong></td>
                  <td>Advance Payments: Initial 40% Retainer</td>
                  <td>$180,000</td>
                  <td><span class="status-badge badge-confirmed">Payment Confirmation Verified</span></td>
                  <td><button class="table-btn table-btn-ghost">Download Invoice</button></td>
                </tr>
                <tr>
                  <td><strong>INV-2026-4402</strong></td>
                  <td>Completed Payments: Venue Lock (30%)</td>
                  <td>$135,000</td>
                  <td><span class="status-badge badge-confirmed">Payment Confirmation Verified</span></td>
                  <td><button class="table-btn table-btn-ghost">Download Invoice</button></td>
                </tr>
                <tr>
                  <td><strong>INV-2026-4403</strong></td>
                  <td>Pending Payments: Production & AV (20%)</td>
                  <td>$90,000</td>
                  <td><span class="status-badge badge-pending">Due in 14 Days</span></td>
                  <td><button class="table-btn table-btn-primary">Initiate Wire</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 12: COMMUNICATION
           ====================================================================== -->
      <section class="module-view" id="view-client-communication">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Executive Communication & Discussion Threads</h1>
            <p>Direct priority line to your dedicated Event Director Elena Rostova, meeting notes, project updates, and support.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="openModal('meetingRequestModal')"><i class="fas fa-calendar-plus"></i> Meeting Requests</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Messages to Event Manager</button>
          <button class="subfeature-chip">Project Discussion Threads</button>
          <button class="subfeature-chip" onclick="openModal('meetingRequestModal')">Meeting Requests</button>
          <button class="subfeature-chip">Meeting Notes</button>
          <button class="subfeature-chip">Event Update Notifications</button>
          <button class="subfeature-chip">Support Requests</button>
        </div>

        <div class="panel-card">
          <!-- Discussion Thread Box -->
          <div style="padding: 1.25rem; border-radius: 0.85rem; background: var(--adm-surface-card); border: 1px solid var(--adm-border-subtle); margin-bottom: 1.5rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.85rem;">
              <span style="font-weight:700; color:var(--adm-text-primary); font-size:0.95rem;">
                <i class="fas fa-comments text-sky-400"></i> Direct Channel: Elena Rostova (Lead Producer)
              </span>
              <span class="status-badge badge-confirmed">Online &bull; Active Node</span>
            </div>
            
            <div style="display:flex; flex-direction:column; gap:0.75rem; max-height:220px; overflow-y:auto; padding-right:0.5rem; margin-bottom:1rem;">
              <div style="background:rgba(255,255,255,0.05); padding:0.75rem 1rem; border-radius:0.75rem; border-left:3px solid #2563eb;">
                <strong style="color:var(--adm-text-primary); font-size:0.82rem;">Elena Rostova:</strong>
                <p style="font-size:0.84rem; margin-top:0.25rem;">"Lord Julian, the acoustic isolation test for the Geneva Plenary passed with flying colors at -52dB. All 16 language booths are confirmed."</p>
                <span style="font-size:0.7rem; color:var(--adm-text-muted);">Today at 11:42 CET</span>
              </div>
              <div style="background:rgba(37,99,235,0.12); padding:0.75rem 1rem; border-radius:0.75rem; border-left:3px solid #10b981; margin-left:1.5rem;">
                <strong style="color:#60a5fa; font-size:0.82rem;">Lord Julian Sterling:</strong>
                <p style="font-size:0.84rem; margin-top:0.25rem;">"Excellent work, Elena. Let us ensure the G7 delegation motorcade security detail is briefed prior to our Wednesday dry run."</p>
                <span style="font-size:0.7rem; color:var(--adm-text-muted);">Today at 12:15 CET</span>
              </div>
            </div>

            <!-- Message Input Form -->
            <form onsubmit="event.preventDefault(); alert('Message dispatched to Elena Rostova!');" style="display:flex; gap:0.75rem;">
              <input type="text" class="form-control" placeholder="Type direct message to Event Director..." required>
              <button type="submit" class="btn-action-primary" style="flex-shrink:0;"><i class="fas fa-paper-plane"></i> Send</button>
            </form>
          </div>
        </div>
      </section>

      <!-- ======================================================================
           MODULE 13: FEEDBACK & REVIEWS
           ====================================================================== -->
      <section class="module-view" id="view-feedback-reviews">
        <div class="module-header">
          <div class="header-left-col">
            <h1>Feedback, Quality Reviews & Final Reports</h1>
            <p>Submit post-event feedback, rate service delivery, report issues, and download final event outcome summaries.</p>
          </div>
          <div class="header-actions-col">
            <button class="btn-action-primary" onclick="alert('Downloading Final Event Report (PDF)...')"><i class="fas fa-download"></i> Download Final Event Report</button>
          </div>
        </div>

        <div class="subfeature-chips-bar">
          <button class="subfeature-chip active">Submit Event Feedback</button>
          <button class="subfeature-chip">Rate Event Services</button>
          <button class="subfeature-chip">Report Event Issues</button>
          <button class="subfeature-chip">Review Event Outcomes</button>
          <button class="subfeature-chip" onclick="alert('Downloading...')">Download Final Event Report</button>
        </div>

        <div class="panel-card" style="max-width: 850px;">
          <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--adm-text-primary); margin-bottom: 1rem;">
            <i class="fas fa-star" style="color: #fbbf24;"></i> Submit Event Feedback & Service Ratings
          </h3>
          <p style="font-size: 0.9rem; color: var(--adm-text-secondary); margin-bottom: 1.5rem;">
            Your feedback directly calibrates EventSphere's sovereign delivery standards and vendor performance scoring.
          </p>

          <form onsubmit="event.preventDefault(); alert('Thank you! Your executive feedback has been submitted to the Executive Board.');">
            <div class="form-group">
              <label class="form-label">Rate Overall Conference Execution & Quality</label>
              <div style="display:flex; gap:0.75rem; font-size:1.5rem; color:#fbbf24; cursor:pointer;">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Audio-Visual & Spatial Acoustic Performance</label>
              <select class="form-control">
                <option>Exceptional (100% Zero-Drop Telemetry)</option>
                <option>High Quality</option>
                <option>Satisfactory</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Review Event Outcomes & Executive Highlights</label>
              <textarea class="form-control" rows="3" placeholder="Provide qualitative insights on delegate engagement, M&A deal flow, and sovereign protocol satisfaction..."></textarea>
            </div>

            <button type="submit" class="btn-action-primary"><i class="fas fa-paper-plane"></i> Submit Event Feedback</button>
          </form>
        </div>
      </section>

    </main>
  </div>

  <!-- ==========================================================================
       MODALS: CREATE EVENT, MEETING REQUEST & LOGOUT
       ========================================================================== -->
  <!-- 1. Submit Event Requirements Modal -->
  <div class="admin-modal-overlay" id="createEventModal">
    <div class="admin-modal-box">
      <div class="modal-header-row">
        <h3><i class="fas fa-calendar-plus" style="color: #2563eb;"></i> Submit Event Requirements</h3>
        <button class="modal-close-btn" onclick="closeModal('createEventModal')"><i class="fas fa-times"></i></button>
      </div>
      <form onsubmit="handleModalSubmit(event, 'Event Requirements Submitted! Your Event Director will prepare customized proposals.')">
        <div class="form-group">
          <label class="form-label">Event Name & Type *</label>
          <input type="text" class="form-control" required placeholder="e.g. World FinTech Sovereign Summit 2027">
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
          <div class="form-group">
            <label class="form-label">Event Date & Duration *</label>
            <input type="text" class="form-control" required placeholder="e.g. Nov 14 - 17, 2027 (4 Days)">
          </div>
          <div class="form-group">
            <label class="form-label">Expected Attendee Count *</label>
            <input type="number" class="form-control" required placeholder="e.g. 5800">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Preferred Location & Host City</label>
          <input type="text" class="form-control" placeholder="e.g. Geneva, Switzerland or London Mayfair">
        </div>
        <div class="form-group">
          <label class="form-label">Strategic Event Objectives</label>
          <textarea class="form-control" rows="2" placeholder="Describe the strategic balance sheet outcomes, dealmaking goals, or ministerial accords..."></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Special Requirements</label>
          <input type="text" class="form-control" placeholder="e.g. 432Hz psychoacoustic tuning, biometric kiosks, 16 translation booths">
        </div>
        <div class="form-group">
          <label class="form-label">Upload Event Documents (Briefings, RFPs, Floorplans)</label>
          <input type="file" class="form-control">
        </div>
        <button type="submit" class="btn-action-primary" style="width: 100%; justify-content: center; margin-top: 1rem;">
          <i class="fas fa-check-circle"></i> Transmit Requirements to Event Director
        </button>
      </form>
    </div>
  </div>

  <!-- 2. Meeting Request Modal -->
  <div class="admin-modal-overlay" id="meetingRequestModal">
    <div class="admin-modal-box">
      <div class="modal-header-row">
        <h3><i class="fas fa-calendar-check" style="color: #10b981;"></i> Schedule Meeting with Event Director</h3>
        <button class="modal-close-btn" onclick="closeModal('meetingRequestModal')"><i class="fas fa-times"></i></button>
      </div>
      <form onsubmit="handleModalSubmit(event, 'Meeting request dispatched to Elena Rostova! Calendar invite sent.')">
        <div class="form-group">
          <label class="form-label">Meeting Topic / Agenda *</label>
          <input type="text" class="form-control" required placeholder="e.g. Review Plenary 360 Stage Mockup & Security Protocol">
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
          <div class="form-group">
            <label class="form-label">Preferred Date</label>
            <input type="date" class="form-control">
          </div>
          <div class="form-group">
            <label class="form-label">Preferred Time (CET)</label>
            <input type="time" class="form-control" value="14:00">
          </div>
        </div>
        <button type="submit" class="btn-action-primary" style="width: 100%; justify-content: center; margin-top: 1rem; background: linear-gradient(135deg, #059669, #10b981);">
          <i class="fas fa-video"></i> Confirm Briefing Request
        </button>
      </form>
    </div>
  </div>

  <!-- 3. Logout Confirmation Modal -->
  <div class="admin-modal-overlay" id="logoutModal">
    <div class="admin-modal-box" style="max-width: 440px; text-align: center;">
      <div style="font-size: 3rem; color: #f43f5e; margin-bottom: 1rem;">
        <i class="fas fa-sign-out-alt"></i>
      </div>
      <h3 style="font-size: 1.45rem; font-weight: 800; color: var(--adm-text-primary); margin-bottom: 0.5rem;">
        Confirm Portal Logout
      </h3>
      <p style="font-size: 0.92rem; color: var(--adm-text-muted); margin-bottom: 1.75rem;">
        Are you sure you wish to exit your executive client portal session?
      </p>
      <div style="display: flex; gap: 0.75rem; justify-content: center;">
        <button class="btn-action-ghost" onclick="closeModal('logoutModal')">Cancel</button>
        <button class="btn-action-primary" style="background: #f43f5e; border-color: #f43f5e;" onclick="window.location.href='index.html'">
          Confirm & Exit
        </button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       JAVASCRIPT LOGIC
       ========================================================================== -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // 1. Clone Navigation to Mobile Drawer
      const desktopList = document.getElementById('mainSidebarList');
      const drawerList = document.getElementById('drawerMenuList');
      if (desktopList && drawerList) {
        drawerList.innerHTML = desktopList.innerHTML;
      }

      // 2. Hamburger & Mobile Drawer Toggling
      const hamburgerBtn = document.getElementById('hamburgerBtn');
      const closeDrawerBtn = document.getElementById('closeDrawerBtn');
      const mobileDrawer = document.getElementById('mobileDrawer');
      const drawerBackdrop = document.getElementById('drawerBackdrop');

      function openDrawer() {
        mobileDrawer.classList.add('open');
        drawerBackdrop.classList.add('open');
        document.body.style.overflow = 'hidden';
      }

      function closeDrawer() {
        mobileDrawer.classList.remove('open');
        drawerBackdrop.classList.remove('open');
        document.body.style.overflow = '';
      }

      if (hamburgerBtn) hamburgerBtn.addEventListener('click', openDrawer);
      if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeDrawer);
      if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

      // 3. Module Tab Switching (Both Desktop & Drawer)
      function attachNavListeners() {
        const allNavItems = document.querySelectorAll('.nav-module-item');
        allNavItems.forEach(item => {
          item.addEventListener('click', function(e) {
            e.preventDefault();
            const mod = this.getAttribute('data-module');
            if (!mod) {
              if (this.classList.contains('logout-item') || this.id === 'sidebarLogoutBtn') {
                openModal('logoutModal');
              }
              return;
            }

            // Update active state in both desktop & drawer lists
            allNavItems.forEach(i => {
              if (i.getAttribute('data-module') === mod) {
                i.classList.add('active');
              } else {
                i.classList.remove('active');
              }
            });

            // Switch view
            const allViews = document.querySelectorAll('.module-view');
            allViews.forEach(v => v.classList.remove('active'));
            const targetView = document.getElementById('view-' + mod);
            if (targetView) {
              targetView.classList.add('active');
            }

            // Close mobile drawer if open
            closeDrawer();
            window.scrollTo({ top: 0, behavior: 'smooth' });
          });
        });
      }
      attachNavListeners();

      // 4. Dark / Light Theme Toggle
      const themeToggleBtn = document.getElementById('themeToggleBtn');
      const drawerThemeBtn = document.getElementById('drawerThemeBtn');

      function toggleTheme() {
        document.body.classList.toggle('light');
        const isLight = document.body.classList.contains('light');
        const icon = isLight ? '<i class="fas fa-sun" style="color: #f59e0b;"></i>' : '<i class="fas fa-moon"></i>';
        if (themeToggleBtn) themeToggleBtn.innerHTML = icon;
        if (drawerThemeBtn) drawerThemeBtn.innerHTML = icon + ' Theme';
      }

      if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);
      if (drawerThemeBtn) drawerThemeBtn.addEventListener('click', toggleTheme);

      // 5. RTL Toggle
      const rtlToggleBtn = document.getElementById('rtlToggleBtn');
      const drawerRtlBtn = document.getElementById('drawerRtlBtn');

      function toggleRtl() {
        document.body.classList.toggle('rtl');
      }

      if (rtlToggleBtn) rtlToggleBtn.addEventListener('click', toggleRtl);
      if (drawerRtlBtn) drawerRtlBtn.addEventListener('click', toggleRtl);

      // 6. Refresh Metrics Simulation
      const refreshBtn = document.getElementById('refreshMetricsBtn');
      if (refreshBtn) {
        refreshBtn.addEventListener('click', function() {
          const icon = this.querySelector('i');
          if (icon) icon.classList.add('fa-spin');
          setTimeout(() => {
            if (icon) icon.classList.remove('fa-spin');
            alert('Live Summit Metrics Synchronized from Geneva Operations Node!');
          }, 600);
        });
      }

      // 7. Shortcut (Ctrl + K) for Quick Search
      window.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
          e.preventDefault();
          const searchInput = document.getElementById('topbarSearchInput');
          if (searchInput && window.innerWidth > 1120) {
            searchInput.focus();
          } else {
            openDrawer();
            const drawerSearch = document.getElementById('drawerSearchInput');
            if (drawerSearch) drawerSearch.focus();
          }
        }
        if (e.key === 'Escape') {
          closeDrawer();
          closeAllModals();
        }
      });
    });

    // Global Modal Helpers
    function openModal(id) {
      const m = document.getElementById(id);
      if (m) m.classList.add('open');
    }

    function closeModal(id) {
      const m = document.getElementById(id);
      if (m) m.classList.remove('open');
    }

    function closeAllModals() {
      document.querySelectorAll('.admin-modal-overlay').forEach(m => m.classList.remove('open'));
    }

    function handleModalSubmit(e, successMsg) {
      e.preventDefault();
      alert(successMsg);
      closeAllModals();
    }

    function switchModule(moduleName) {
      const targetBtn = document.querySelector(`.nav-module-item[data-module="${moduleName}"]`);
      if (targetBtn) targetBtn.click();
    }
  </script>
</body>
</html>
"""

    with open('user-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Successfully generated user-dashboard.html! Length:", len(html_content))

if __name__ == '__main__':
    generate_user_dashboard()
