from django.shortcuts import render_to_response

def issues(request):
    return render_to_response("issues.html", {})
