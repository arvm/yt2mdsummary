from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url):
    import re
    match = re.search(r"v=([a-zA-z0-9_-]{11})", url)
    return match.group(1) if match else None


def fetch_transcript(video_id, filename="transcript.txt"):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = "\n".join([t['text'] for t in transcript])
    with open(filename, "w", encoding='utf-8') as f:
        f.write(full_text)
    return full_text


if __name__ == "__main__":
    url = input("Please enter a youtube url: ")
    video_id = get_video_id(url)

    print("Fetching transcript...")
    fetch_transcript(video_id)
