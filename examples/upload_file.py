import asyncio
import argparse
from pathlib import Path

from runwayml import RunwayML, AsyncRunwayML

parser = argparse.ArgumentParser(description="Upload a file to RunwayML")
parser.add_argument("--file", required=True, type=Path, help="Path to the file to upload")
parser.add_argument("-i", action="store_true", help="Generate an image with the uploaded file")
parser.add_argument("--async", action="store_true", dest="use_async", help="Use async client")
args = parser.parse_args()

file_path = args.file

if not file_path.exists():
    parser.error(f"File not found: {file_path}")


async def async_upload() -> None:
    client = AsyncRunwayML()
    upload_response = await client.uploads.create_ephemeral(file=file_path)
    print(f"Upload successful! URI: {upload_response.uri}")
    
    if args.i:
        image_task = await client.text_to_image.create(
            model="gen4_image",
            prompt_text="add a bunny",
            ratio="1920:1080",
            reference_images=[{"uri": upload_response.uri}],
        )
        print(await image_task.wait_for_task_output())


def sync_upload() -> None:
    client = RunwayML()
    upload_response = client.uploads.create_ephemeral(file=file_path)
    print(f"Upload successful! URI: {upload_response.uri}")
    
    if args.i:
        image_task = client.text_to_image.create(
            model="gen4_image",
            prompt_text="add a bunny",
            ratio="1920:1080",
            reference_images=[{"uri": upload_response.uri}],
        )
        print(image_task.wait_for_task_output())


if args.use_async:
    asyncio.run(async_upload())
else:
    sync_upload()