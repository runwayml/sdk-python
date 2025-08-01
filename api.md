# Tasks

Types:

```python
from runwayml.types import TaskRetrieveResponse
```

Methods:

- <code title="get /v1/tasks/{id}">client.tasks.<a href="./src/runwayml/resources/tasks.py">retrieve</a>(id) -> <a href="./src/runwayml/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="delete /v1/tasks/{id}">client.tasks.<a href="./src/runwayml/resources/tasks.py">delete</a>(id) -> None</code>

# ImageToVideo

Types:

```python
from runwayml.types import ImageToVideoCreateResponse
```

Methods:

- <code title="post /v1/image_to_video">client.image_to_video.<a href="./src/runwayml/resources/image_to_video.py">create</a>(\*\*<a href="src/runwayml/types/image_to_video_create_params.py">params</a>) -> <a href="./src/runwayml/types/image_to_video_create_response.py">ImageToVideoCreateResponse</a></code>

# VideoToVideo

Types:

```python
from runwayml.types import VideoToVideoCreateResponse
```

Methods:

- <code title="post /v1/video_to_video">client.video_to_video.<a href="./src/runwayml/resources/video_to_video.py">create</a>(\*\*<a href="src/runwayml/types/video_to_video_create_params.py">params</a>) -> <a href="./src/runwayml/types/video_to_video_create_response.py">VideoToVideoCreateResponse</a></code>

# TextToImage

Types:

```python
from runwayml.types import TextToImageCreateResponse
```

Methods:

- <code title="post /v1/text_to_image">client.text_to_image.<a href="./src/runwayml/resources/text_to_image.py">create</a>(\*\*<a href="src/runwayml/types/text_to_image_create_params.py">params</a>) -> <a href="./src/runwayml/types/text_to_image_create_response.py">TextToImageCreateResponse</a></code>

# VideoUpscale

Types:

```python
from runwayml.types import VideoUpscaleCreateResponse
```

Methods:

- <code title="post /v1/video_upscale">client.video_upscale.<a href="./src/runwayml/resources/video_upscale.py">create</a>(\*\*<a href="src/runwayml/types/video_upscale_create_params.py">params</a>) -> <a href="./src/runwayml/types/video_upscale_create_response.py">VideoUpscaleCreateResponse</a></code>

# CharacterPerformance

Types:

```python
from runwayml.types import CharacterPerformanceCreateResponse
```

Methods:

- <code title="post /v1/character_performance">client.character_performance.<a href="./src/runwayml/resources/character_performance.py">create</a>(\*\*<a href="src/runwayml/types/character_performance_create_params.py">params</a>) -> <a href="./src/runwayml/types/character_performance_create_response.py">CharacterPerformanceCreateResponse</a></code>

# Organization

Types:

```python
from runwayml.types import OrganizationRetrieveResponse, OrganizationRetrieveUsageResponse
```

Methods:

- <code title="get /v1/organization">client.organization.<a href="./src/runwayml/resources/organization.py">retrieve</a>() -> <a href="./src/runwayml/types/organization_retrieve_response.py">OrganizationRetrieveResponse</a></code>
- <code title="post /v1/organization/usage">client.organization.<a href="./src/runwayml/resources/organization.py">retrieve_usage</a>(\*\*<a href="src/runwayml/types/organization_retrieve_usage_params.py">params</a>) -> <a href="./src/runwayml/types/organization_retrieve_usage_response.py">OrganizationRetrieveUsageResponse</a></code>
