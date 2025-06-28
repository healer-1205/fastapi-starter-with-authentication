from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config import oauth
from app.dependencies import get_db
from app.controllers.UserController import create_user_from_oauth
from authlib.integrations.starlette_client import OAuthError
from starlette.requests import Request
from starlette.responses import RedirectResponse

router = APIRouter(prefix="/auth", tags=["oauth"])


@router.get("/google")
async def login_via_google(request: Request):
    redirect_uri = request.url_for("auth_google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/callback")
async def auth_google_callback(request: Request, db: Session = Depends(get_db)):
    try:
        token = await oauth.google.authorize_access_token(request)
        user_info = await oauth.google.parse_id_token(request, token)

        # Extract user information
        email = user_info.get("email")
        name = user_info.get("name")
        google_id = user_info.get("sub")

        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")

        # Create or get user from database
        user = await create_user_from_oauth(db, email, name, google_id)

        # Create your own JWT token here
        # You can use your existing JWT logic from UserController

        # Redirect to frontend with token
        frontend_url = "http://localhost:5173"  # Your frontend URL
        return RedirectResponse(url=f"{frontend_url}?token=your-jwt-token-here")

    except OAuthError:
        raise HTTPException(status_code=400, detail="Google authentication failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Authentication error: {str(e)}")
