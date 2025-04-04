import yt_dlp
from flask import Flask, request, send_file,render_template

app = Flask(__name__)

@app.route('/upload', methods=['POST'])

def home():
    return render_template("index.html")

def download_video():
    try:
        #URL from the form input
        video_url = request.form['yfile']
        print(f"Downloading video from: {video_url}")
        
        #filename for the downloaded video
        video_title = "downloaded_video.mp4"
        
        # yt-dlp options
        ydl_opts = {
            'format': 'best',  #best quality video
            'outtmpl': video_title  # Save to a specific local file
        }

        # Download the video
        ydl=yt_dlp.YoutubeDL(ydl_opts)
        ydl.download([video_url])

        # Serve the file to the user
        return send_file(
            video_title,
            mimetype='video/mp4',
            as_attachment=True,
            download_name='video.mp4'
        )
    except Exception as e:
        return f"An error occurred: {e}", 500


if __name__ == "__main__":
    # Make the server accessible from other devices on the network
    app.run(debug=True)
