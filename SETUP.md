# Setup Instructions

## Prerequisites
- Python 3.8+
- Virtual environment activated
- Dependencies installed: `pip install -r requirements.txt`

## Configuration

### Step 1: Get Your OpenAI API Key
1. Go to https://platform.openai.com/account/api-keys
2. Create a new API key (or use an existing one)
3. Copy the key (it starts with `sk-`)

### Step 2: Configure the .env File
Edit the `.env` file in the project root and add your actual API key:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

⚠️ **Important:** Replace `your-actual-api-key-here` with your real OpenAI API key
⚠️ **Security:** Never commit the .env file with your API key to version control

### Step 3 (Optional): HuggingFace Token
If you want to use HuggingFace models, also add:

```
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
```

## Running the Application

### Frontend (Streamlit Web App)
```bash
streamlit run app.py
```
The app will open at `http://localhost:8501` or `http://localhost:8502`

### Backend (Jupyter Notebook)
```bash
jupyter notebook Notebook_Experiments/Experiment.ipynb
```
Or run it directly with VS Code's Notebook interface.

## Troubleshooting

### Error: "Incorrect API key provided"
- Check that your API key is correct in the `.env` file
- Ensure there are no extra spaces or quotes around the key
- Verify the key hasn't been revoked on OpenAI's website

### Error: "OPENAI_API_KEY not set"
- Make sure `.env` file exists in the project root
- Check that `OPENAI_API_KEY=` is not empty
- Restart the Streamlit/Jupyter app after updating .env

### Module Not Found Errors
- Reinstall dependencies: `pip install -r requirements.txt`
- For notebook: run `pip install -r requirements.txt` in the kernel

## Features

✅ **Frontend (Streamlit)**
- Interactive chatbot interface
- Real-time query processing
- Error handling and user guidance

✅ **Backend (Jupyter Notebook)**
- LLM experimentation with OpenAI
- PromptTemplate examples
- ChatOpenAI integration
- Output parser demonstrations
- Sequential and standalone chain examples

## API Costs
⚠️ **Note:** Each API call to OpenAI will incur charges based on your plan. Monitor your usage at https://platform.openai.com/account/usage/overview
