# Automation Portfolio Log & Roadmap

This file is your living document. It tracks your goals, daily progress, and lessons learned.

## 🛣️ Roadmap

### Phase 1: Foundation
- [x] **Setup Project**: Follow `setup_guide.md` to install Python, Playwright, and create venv.
- [ ] **First Script**: Write a simple script to open `https://automationexercise.com/` and verify the title.
- [x] **Project Structure**: Create `tests/`, `pages/`, and `utils/` folders.

### Phase 2: Page Object Model (POM) (Current)
- [x] **Create BasePage**: A common class for shared methods (click, type, find).
- [/] **Implement Login Page**: Specific page class for the Login functionality.
- [ ] **Implement Config**: Add base URL and other settings to `utils/config.py`.
- [ ] **Write First Test**: Create a login test using the Page Object.

### Phase 3: Expanding Coverage
- [ ] **Registration Flow**: Automate user signup.
- [ ] **Product Cart**: Automate adding items to cart.
- [ ] **Checkout**: Automate the checkout process.

### Phase 4: Advanced & Reporting
- [ ] **Reporting**: Integrate `pytest-html` or Allure for nice reports.
- [ ] **CI/CD**: Create a GitHub Actions workflow to run tests on push.

---

## 📝 Progress Log

### [Date: 2025-12-22]
*   **Things I did**:
    *   Created `venv` and installed dependencies (`requirements.txt`).
    *   Set up project structure: `pages/`, `tests/`, `utils/`.
    *   Created `BasePage` class in `pages/base_page.py` with `click`, `type`, and `get_text` methods.
    *   Started `LoginPage` class (currently empty).
*   **Walkthrough / Notes**:
    *   The `BasePage` uses `logging` to record actions—great for debugging!
    *   Next: Implement `LoginPage` and the `Config` class.

---

## 💡 Notes & Resources
- **Site**: [Automation Exercise](https://automationexercise.com/)
- **Docs**: [Playwright Python Docs](https://playwright.dev/python/docs/intro)
