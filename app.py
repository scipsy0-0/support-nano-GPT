import gradio as gr
from runner import gen


demo = gr.Interface(
    fn=gen,
    inputs="text",
    outputs="text",
    examples=[
        ["Where do deleted files go?"],
        ["How long do files stay in the Trash?"],
        ["Do files in the Trash take up space?"],
        ["What format are folders downloaded in?"],
        ["How do I sort files?"],
        ["How many files can I select at once?"],
        ["How do I get a photo in its original quality?"],
        ["How do I play a video?"],
        ["What is the maximum video playback quality on the website?"],
        ["Are document changes saved automatically?"],
        ["How many users can edit a document at the same time?"],
        ["Can I edit XLSX spreadsheets on Yandex Disk?"],
    ],
    article="""
### Examples

| Question | Answer |
|---|---|
| Where do deleted files go? | Deleted files go to the Trash on Yandex Disk server |
| How long do files stay in the Trash? | Files stay in the Trash for 30 days |
| Do files in the Trash take up space? | Yes, files in the Trash take up space on Yandex Disk |
| What format are folders downloaded in? | Folder download is downloaded as ZIP archives |
| How do I sort files? | Sort files in a folder |
| How many files can I select at once? | You can select multiple files at once |
| How do I get a photo in its original quality? | To get a photo in its original quality, download it to your computer and double-click an image to view it in full-screen mode |
| How do I play a video? | To play a video, double-click it and click the play button in the window that appears |
| What is the maximum video playback quality on the website? | The maximum video playback quality on the website is 1080p |
| Are document changes saved automatically? | Yes, document changes are saved automatically |
| How many users can edit a document at the same time? | There are 40 users able to edit a document at the same time |
| Can I edit XLSX spreadsheets on Yandex Disk? | Yes, you can edit XLSX spreadsheets on Yandex Disk |
""",
)

demo.launch()