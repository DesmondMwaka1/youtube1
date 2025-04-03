from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)  # Fix for reverse proxy issues with Flask in Vercel

@app.route('/upload', methods=['POST'])
def download_video():
    video_url = request.form['yfile']
    print(f"Downloading video from: {video_url}")
    
    # Temporary storage for serverless environments
    video_title = "/tmp/downloaded_video.mp4"
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': video_title
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return send_file(video_title, mimetype='video/mp4', as_attachment=True, download_name='video.mp4')

# Use this for Vercel
from vercel_wsgi import handle
handler = handle(app)
