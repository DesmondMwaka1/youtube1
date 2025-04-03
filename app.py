import yt_dlp
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def download_video():
    #URL from the form input
    video_url = request.form['yfile']
    print(f"Downloading video from: {video_url}")
        
    #temporary storage for the downloaded video
    video_title = "/tmp/downloaded_video.mp4"  # Use /tmp directory for serverless storage
        
    # yt-dlp options
    options = {
        'format': 'best',  # best quality video
        'outtmpl': video_title  # Save to the /tmp directory
    }

    # Download the video
    ydl=yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([video_url])

    # Serve the file to the user
    return send_file(video_title, mimetype='video/mp4', as_attachment=True, download_name='video.mp4')

# Vercel requires a function named "handler" for serverless deployment
def handler(event, context):
    return app(event, context)
