import gradio as gr
from runner import gen


demo = gr.Interface(
    fn=gen,
    inputs="text",
    outputs="text",
    examples=[
        ["Where do deleted files go?"],
        ["Can I select 600 files at once?"],
        ["Are photos compressed during upload?"],
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

| Question | Answer | Waited ans |
|---|---|---|
| Where do deleted files go? | Deleted files go to the Trash on Yandex Disk server | Deleted files go to the Trash. |
| Can I select 600 files at once? | Yes, you can select 600 files at once | No, you can select up to 500 files at once. |
| Are photos compressed during upload? | Yes, photos are compressed during upload | No, their original quality is preserved. |
| How long do files stay in the Trash? | Files stay in the Trash for 30 days | Files stay in the Trash for 30 days. |
| Do files in the Trash take up space? | Yes, files in the Trash take up space on Yandex Disk | Yes, files in the Trash still take up space. |
| What format are folders downloaded in? | Folder download is downloaded as ZIP archives | Folders are downloaded as ZIP archives. |
| How do I sort files? | Sort files in a folder | Click Sort and choose a sorting option. |
| How many files can I select at once? | You can select multiple files at once | You can select up to 500 files at once. |
| How do I get a photo in its original quality? | To get a photo in its original quality, download it to your computer and double-click an image to view it in full-screen mode | Download the photo to your computer to view it in its original quality. |
| How do I play a video? | To play a video, double-click it and click the play button in the window that appears | Double-click the video. |
| What is the maximum video playback quality on the website? | The maximum video playback quality on the website is 1080p | The maximum video playback quality on the website is 1080p. |
| Are document changes saved automatically? | Yes, document changes are saved automatically | Yes, all changes are saved automatically. |
| How many users can edit a document at the same time? | There are 40 users able to edit a document at the same time | Up to 40 users can edit a document at the same time. |
| Can I edit XLSX spreadsheets on Yandex Disk? | Yes, you can edit XLSX spreadsheets on Yandex Disk | Yes, Yandex Disk supports editing XLSX spreadsheets. |
""",
)

demo.launch()