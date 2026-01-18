# Quick Reference Card - LangChain Chatbot

## ⚡ Quick Start

**Open Browser**: http://localhost:8501

**Ask Question**: Type in input box → Click Submit

**Wait**: 5-10 seconds for processing

**Review**: See answer + confidence + bias status

---

## 🟢 System Status

| Component | Status | Details |
|-----------|--------|---------|
| **Frontend** | ✅ Running | Streamlit at http://localhost:8501 |
| **Backend** | ✅ Connected | Groq API with llama-3.3-70b-versatile |
| **Verification** | ✅ Active | 4-step chain active |
| **API Key** | ✅ Configured | .env file has GROQ_API_KEY |
| **Python** | ✅ Ready | Version 3.14 in virtual environment |

---

## 📊 What You'll See

```
Query Input
    ↓
Processing with verification chain...
    ↓
┌─────────────────────────────────┐
│ Answer: [Your answer]           │
├─────────────────────────────────┤
│ Confidence: 🟢 High             │
│ Bias: ✅ No Bias                │
│ Response: ✅ Original           │
├─────────────────────────────────┤
│ [View Verification Details ▼]   │
└─────────────────────────────────┘
```

---

## 🎯 Test Queries

### Easy (High Confidence Expected)
```
- What is the capital of France?
- What is 2+2?
- Who invented electricity?
```

### Medium (Variable Confidence)
```
- Is artificial intelligence good?
- Should social media be regulated?
- What is the best programming language?
```

### Hard (Low Confidence Expected)
```
- What will happen in 2050?
- Is [stereotype] true about [group]?
- Predict the stock market tomorrow
```

---

## 📈 Metrics Explained

### Confidence Level
- 🟢 **High**: Verified facts, factually correct
- 🟡 **Medium**: Mostly accurate, some issues
- 🔴 **Low**: Uncertain, may need refinement

### Bias Status
- ✅ **No Bias**: Objective, balanced response
- ⚠️ **Possible Bias**: One-sided, subjective language

### Response Type
- ✅ **Original**: Verified, no issues found
- 🔄 **Refined**: Improved based on verification

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't open http://localhost:8501 | Check terminal for "Local URL" message |
| "API key not found" | Verify .env has GROQ_API_KEY |
| Slow response (>30 sec) | Verification takes 5-10 sec, normal |
| All queries "Low confidence" | Try factual queries (capitals, math) |
| API errors | Check internet, verify API key validity |

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| **app.py** | Main Streamlit frontend |
| **.env** | API configuration |
| **VERIFICATION_SYSTEM.md** | How verification works |
| **TESTING_GUIDE.md** | Test queries & scenarios |
| **IMPLEMENTATION_SUMMARY.md** | Technical details |

---

## 🔍 Verification Steps

The system runs 4 steps automatically:

1. **Generate** - Create initial response
2. **Verify** - Check accuracy & bias
3. **Score** - Assess confidence level
4. **Refine** - Improve if issues found

All steps take 5-10 seconds total.

---

## ✅ What's Working

- ✅ Hallucination prevention
- ✅ Bias detection & correction
- ✅ Confidence scoring
- ✅ Response refinement
- ✅ Clean UI
- ✅ Error handling
- ✅ Full documentation

---

## 🎓 Example Usage

```
You: "What is the capital of India?"

System: Processing with verification chain...

Result:
Answer: The capital of India is New Delhi...

Metrics:
Confidence: 🟢 High
Bias: ✅ No Bias  
Type: ✅ Original

Verification Details:
Accuracy: Yes ✓
Bias: No ✓
Confidence: High ✓
Issues: None
```

---

## 💡 Pro Tips

1. **Factual queries** → Get High confidence
2. **Opinion queries** → May see bias detection
3. **Future events** → Will likely be Low confidence
4. **Click "Details"** → See full analysis
5. **Multiple queries** → Try different categories

---

## 🔗 Quick Links

- **Frontend**: http://localhost:8501
- **Docs**: See VERIFICATION_SYSTEM.md
- **Tests**: See TESTING_GUIDE.md
- **Setup**: See SETUP.md

---

## 📞 Need Help?

**Frontend Not Loading?**
- Check: http://localhost:8501 in browser
- Terminal should show "Local URL: http://localhost:8501"

**API Errors?**
- Check .env file
- Verify GROQ_API_KEY is set
- Check internet connection

**Slow Responses?**
- Verification takes time (multiple API calls)
- 5-10 seconds is normal
- Not a problem, expected behavior

**Questions About Results?**
- Click "View Verification Details"
- Read VERIFICATION_SYSTEM.md
- See TESTING_GUIDE.md for examples

---

**System Ready! 🚀**

Visit http://localhost:8501 to start chatting!
