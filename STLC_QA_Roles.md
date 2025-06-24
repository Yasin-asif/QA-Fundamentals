# 📘 STLC – Software Testing Life Cycle

## 🔍 What is STLC?

The Software Testing Life Cycle (STLC) is a systematic process used by QA teams to ensure software quality. It defines a sequence of activities to be performed during the testing of software.

---

## 📊 STLC Phases & QA Responsibilities

### ✅ Phase 1: Requirement Analysis
- Review functional and non-functional requirements
- Identify testable features
- Communicate ambiguities to stakeholders

### ✅ Phase 2: Test Planning
- Define test scope, objectives, resources
- Select testing tools
- Create risk mitigation strategy
- Finalize timelines

### ✅ Phase 3: Test Case Development
- Design high-quality test cases
- Prepare test data
- Define expected results clearly

### ✅ Phase 4: Test Environment Setup
- Set up required hardware/software
- Configure test servers and devices
- Ensure data availability

### ✅ Phase 5: Test Execution
- Execute test cases systematically
- Log defects in bug tracker
- Retest resolved issues

### ✅ Phase 6: Test Closure
- Evaluate exit criteria
- Prepare test summary report
- Archive test deliverables

---

## ✍️ Example: Gmail Login Feature

| Phase | QA Action | Notes |
|-------|-----------|-------|
| Requirement Analysis | "Login should support all email formats" | Clarified with Product Owner |
| Test Planning | Choose browsers and OS | Chrome, Firefox on Win10 |
| Test Case Development | TC001: Login with valid credentials | Expected: Successful login |
| Test Environment Setup | Configure test DB and browser | Dummy test user: qa_user@gmail.com |
| Test Execution | Bug found on Safari browser | Bug ID: GMAIL-22 |
| Test Closure | Sent test summary email | 12 passed, 3 failed, 2 deferred |

---

## 🧠 Conclusion

STLC is not just about executing tests — it’s about **planning, designing, and improving quality from the beginning**. Every successful QA engineer uses STLC as a **backbone** for professional testing.
