## Imports
import os
import pickle
from typing import Optional, List, Dict, Any, Tuple
import pandas as pd

import os
from fastapi import FastAPI,HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
tmdb_api_key =  os.getenv('tmdb_api_key')

tmdb_base = "https://api.themoviedb.org/3"
tmdb_img_500 = "https://image.tmdb.org/t/p/w500"

if not tmdb_api_key:
    raise RuntimeError('tmdb api key is missing. Put it in .env as tmdb_api_key=xxxx')

app = FastAPI(title="Movie Recommender API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base_dir = os.path.dirname(os.path.abspath(__file__))
model_folder = 'model'

path_df = os.path.join(base_dir, model_folder, "df.pkl")
path_incides = os.path.join(base_dir, model_folder, "indices.pkl")
path_tfidf_matrix = os.path.join(base_dir, model_folder, "tfidf_matrix.pkl")
path_tfidf = os.path.join(base_dir, model_folder, "tfidf.pkl")

## print(f'Baby xxx {base_dir}')

df: Optional[pd.DataFrame] = None
indices_obj: Any = None
tfidf_matrix: Any = None
tfidf_obj: Any = None

title_to_idx: Optional[Dict[str, int]] = None

### to br continued
