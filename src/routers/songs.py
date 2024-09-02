from fastapi import APIRouter, status

from ..services.spotify.downloader import get_spotify_links_from_playlist

# from ..__app_configs import Paths

router: APIRouter = APIRouter(prefix="/v1/songs", tags=["v1/songs"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    description="API to download the songs URls based on the provided criteria",
    summary="Songs URL downloader",
)
async def get_links() -> dict:
    try:
        return get_spotify_links_from_playlist()
    except Exception as err:
        print(err)
