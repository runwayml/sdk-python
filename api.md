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

# TextToVideo

Types:

```python
from runwayml.types import TextToVideoCreateResponse
```

Methods:

- <code title="post /v1/text_to_video">client.text_to_video.<a href="./src/runwayml/resources/text_to_video.py">create</a>(\*\*<a href="src/runwayml/types/text_to_video_create_params.py">params</a>) -> <a href="./src/runwayml/types/text_to_video_create_response.py">TextToVideoCreateResponse</a></code>

# TextToImage

Types:

```python
from runwayml.types import TextToImageCreateResponse
```

Methods:

- <code title="post /v1/text_to_image">client.text_to_image.<a href="./src/runwayml/resources/text_to_image.py">create</a>(\*\*<a href="src/runwayml/types/text_to_image_create_params.py">params</a>) -> <a href="./src/runwayml/types/text_to_image_create_response.py">TextToImageCreateResponse</a></code>

# CharacterPerformance

Types:

```python
from runwayml.types import CharacterPerformanceCreateResponse
```

Methods:

- <code title="post /v1/character_performance">client.character_performance.<a href="./src/runwayml/resources/character_performance.py">create</a>(\*\*<a href="src/runwayml/types/character_performance_create_params.py">params</a>) -> <a href="./src/runwayml/types/character_performance_create_response.py">CharacterPerformanceCreateResponse</a></code>

# TextToSpeech

Types:

```python
from runwayml.types import TextToSpeechCreateResponse
```

Methods:

- <code title="post /v1/text_to_speech">client.text_to_speech.<a href="./src/runwayml/resources/text_to_speech.py">create</a>(\*\*<a href="src/runwayml/types/text_to_speech_create_params.py">params</a>) -> <a href="./src/runwayml/types/text_to_speech_create_response.py">TextToSpeechCreateResponse</a></code>

# SoundEffect

Types:

```python
from runwayml.types import SoundEffectCreateResponse
```

Methods:

- <code title="post /v1/sound_effect">client.sound_effect.<a href="./src/runwayml/resources/sound_effect.py">create</a>(\*\*<a href="src/runwayml/types/sound_effect_create_params.py">params</a>) -> <a href="./src/runwayml/types/sound_effect_create_response.py">SoundEffectCreateResponse</a></code>

# VoiceIsolation

Types:

```python
from runwayml.types import VoiceIsolationCreateResponse
```

Methods:

- <code title="post /v1/voice_isolation">client.voice_isolation.<a href="./src/runwayml/resources/voice_isolation.py">create</a>(\*\*<a href="src/runwayml/types/voice_isolation_create_params.py">params</a>) -> <a href="./src/runwayml/types/voice_isolation_create_response.py">VoiceIsolationCreateResponse</a></code>

# VoiceDubbing

Types:

```python
from runwayml.types import VoiceDubbingCreateResponse
```

Methods:

- <code title="post /v1/voice_dubbing">client.voice_dubbing.<a href="./src/runwayml/resources/voice_dubbing.py">create</a>(\*\*<a href="src/runwayml/types/voice_dubbing_create_params.py">params</a>) -> <a href="./src/runwayml/types/voice_dubbing_create_response.py">VoiceDubbingCreateResponse</a></code>

# SpeechToSpeech

Types:

```python
from runwayml.types import SpeechToSpeechCreateResponse
```

Methods:

- <code title="post /v1/speech_to_speech">client.speech_to_speech.<a href="./src/runwayml/resources/speech_to_speech.py">create</a>(\*\*<a href="src/runwayml/types/speech_to_speech_create_params.py">params</a>) -> <a href="./src/runwayml/types/speech_to_speech_create_response.py">SpeechToSpeechCreateResponse</a></code>

# Organization

Types:

```python
from runwayml.types import OrganizationRetrieveResponse, OrganizationRetrieveUsageResponse
```

Methods:

- <code title="get /v1/organization">client.organization.<a href="./src/runwayml/resources/organization.py">retrieve</a>() -> <a href="./src/runwayml/types/organization_retrieve_response.py">OrganizationRetrieveResponse</a></code>
- <code title="post /v1/organization/usage">client.organization.<a href="./src/runwayml/resources/organization.py">retrieve_usage</a>(\*\*<a href="src/runwayml/types/organization_retrieve_usage_params.py">params</a>) -> <a href="./src/runwayml/types/organization_retrieve_usage_response.py">OrganizationRetrieveUsageResponse</a></code>

# Avatars

Types:

```python
from runwayml.types import (
    AvatarCreateResponse,
    AvatarRetrieveResponse,
    AvatarUpdateResponse,
    AvatarListResponse,
)
```

Methods:

- <code title="post /v1/avatars">client.avatars.<a href="./src/runwayml/resources/avatars.py">create</a>(\*\*<a href="src/runwayml/types/avatar_create_params.py">params</a>) -> <a href="./src/runwayml/types/avatar_create_response.py">AvatarCreateResponse</a></code>
- <code title="get /v1/avatars/{id}">client.avatars.<a href="./src/runwayml/resources/avatars.py">retrieve</a>(id) -> <a href="./src/runwayml/types/avatar_retrieve_response.py">AvatarRetrieveResponse</a></code>
- <code title="patch /v1/avatars/{id}">client.avatars.<a href="./src/runwayml/resources/avatars.py">update</a>(id, \*\*<a href="src/runwayml/types/avatar_update_params.py">params</a>) -> <a href="./src/runwayml/types/avatar_update_response.py">AvatarUpdateResponse</a></code>
- <code title="get /v1/avatars">client.avatars.<a href="./src/runwayml/resources/avatars.py">list</a>(\*\*<a href="src/runwayml/types/avatar_list_params.py">params</a>) -> <a href="./src/runwayml/types/avatar_list_response.py">SyncCursorPage[AvatarListResponse]</a></code>
- <code title="delete /v1/avatars/{id}">client.avatars.<a href="./src/runwayml/resources/avatars.py">delete</a>(id) -> None</code>

# Documents

Types:

```python
from runwayml.types import DocumentCreateResponse, DocumentRetrieveResponse, DocumentListResponse
```

Methods:

- <code title="post /v1/documents">client.documents.<a href="./src/runwayml/resources/documents.py">create</a>(\*\*<a href="src/runwayml/types/document_create_params.py">params</a>) -> <a href="./src/runwayml/types/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /v1/documents/{id}">client.documents.<a href="./src/runwayml/resources/documents.py">retrieve</a>(id) -> <a href="./src/runwayml/types/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
- <code title="get /v1/documents">client.documents.<a href="./src/runwayml/resources/documents.py">list</a>(\*\*<a href="src/runwayml/types/document_list_params.py">params</a>) -> <a href="./src/runwayml/types/document_list_response.py">SyncCursorPage[DocumentListResponse]</a></code>
- <code title="delete /v1/documents/{id}">client.documents.<a href="./src/runwayml/resources/documents.py">delete</a>(id) -> None</code>

# RealtimeSessions

Types:

```python
from runwayml.types import RealtimeSessionCreateResponse, RealtimeSessionRetrieveResponse
```

Methods:

- <code title="post /v1/realtime_sessions">client.realtime_sessions.<a href="./src/runwayml/resources/realtime_sessions.py">create</a>(\*\*<a href="src/runwayml/types/realtime_session_create_params.py">params</a>) -> <a href="./src/runwayml/types/realtime_session_create_response.py">RealtimeSessionCreateResponse</a></code>
- <code title="get /v1/realtime_sessions/{id}">client.realtime_sessions.<a href="./src/runwayml/resources/realtime_sessions.py">retrieve</a>(id) -> <a href="./src/runwayml/types/realtime_session_retrieve_response.py">RealtimeSessionRetrieveResponse</a></code>
- <code title="delete /v1/realtime_sessions/{id}">client.realtime_sessions.<a href="./src/runwayml/resources/realtime_sessions.py">delete</a>(id) -> None</code>

# Voices

Types:

```python
from runwayml.types import (
    VoiceCreateResponse,
    VoiceRetrieveResponse,
    VoiceListResponse,
    VoicePreviewResponse,
)
```

Methods:

- <code title="post /v1/voices">client.voices.<a href="./src/runwayml/resources/voices.py">create</a>(\*\*<a href="src/runwayml/types/voice_create_params.py">params</a>) -> <a href="./src/runwayml/types/voice_create_response.py">VoiceCreateResponse</a></code>
- <code title="get /v1/voices/{id}">client.voices.<a href="./src/runwayml/resources/voices.py">retrieve</a>(id) -> <a href="./src/runwayml/types/voice_retrieve_response.py">VoiceRetrieveResponse</a></code>
- <code title="get /v1/voices">client.voices.<a href="./src/runwayml/resources/voices.py">list</a>(\*\*<a href="src/runwayml/types/voice_list_params.py">params</a>) -> <a href="./src/runwayml/types/voice_list_response.py">SyncCursorPage[VoiceListResponse]</a></code>
- <code title="delete /v1/voices/{id}">client.voices.<a href="./src/runwayml/resources/voices.py">delete</a>(id) -> None</code>
- <code title="post /v1/voices/preview">client.voices.<a href="./src/runwayml/resources/voices.py">preview</a>(\*\*<a href="src/runwayml/types/voice_preview_params.py">params</a>) -> <a href="./src/runwayml/types/voice_preview_response.py">VoicePreviewResponse</a></code>
