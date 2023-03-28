from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

from stable_diffusion_videos import StableDiffusionWalkPipeline
import torch
import mediapy as media

import os
from dotenv import load_dotenv
from pyuploadcare import Uploadcare, File
import psycopg2

load_dotenv()

UC_public_key = os.getenv('UPLOADCARE_PUBLIC_KEY')
UC_secret_key = os.getenv('UPLOADCARE_PRIVATE_KEY')

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_DBNAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
    )
    return conn


video_path = pipeline.walk(prompts, seeds, num_interpolation_steps, height, width, output_dir, name, guidance_scale, num_inference_steps, upsample)

uploadcare = Uploadcare(UC_public_key, UC_secret_key)
uploadcareFile = uploadcare.upload(video_path)
print(uploadcareFile)


with open(video_path, 'rb') as file_object:
     uc_file: File = uploadcare.upload(file_object, store=True)
     print(uc_file.info)
     print(uc_file.original_file_url)

### Database reading and Writing
conn = get_db_connection()
cur = conn.cursor()

##################This is not yet working########## Table not yet created, variables not yet defined
# Insert data into the table
cur.execute('INSERT INTO ai_headlines_table (headline, paragraph, image_url)'
               'VALUES (%s, %s, %s)',
               (textAnswer[0],
               textAnswer[1],
               imgLink)
               )

conn.commit()
cur.close()
conn.close()

print("Generation finished, data inserted to database")

video = media.read_video(video_path)
media.show_video(video, fps=6) 