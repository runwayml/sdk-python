from runwayml import RunwayML, TaskFailedError

client = RunwayML()

image_task = client.text_to_image.create(
    model="gen4_image",
    prompt_text="A beautiful sunset over a calm ocean",
    ratio="1920:1080",
)
try:
    output = image_task.wait_for_task_output()
except TaskFailedError as e:
    print("The image failed to generate.")
    print(e.task_details)
else:
    print(output.output[0])  # type: ignore
