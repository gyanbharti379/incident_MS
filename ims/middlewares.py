from django.shortcuts import render

class VisitorCountMiddleware:
    def __init__(self, get_response):
        print("initial")
        self.get_response = get_response
        self.visitor_count = 0

    def __call__(self, request):
        self.visitor_count += 1
        request.visitor_count = self.visitor_count
        print("before response: visitor count: ", self.visitor_count)

        # Continue to the next middleware or view
        response = self.get_response(request)

        print("after response: visitor count: ", self.visitor_count) 
        return response

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Continue to the next middleware or view
        response = self.get_response(request)

        print("rendering under construction response")
        return render(request, "frontend/under_construction_page.html", {
                    "visitor_count": request.visitor_count
                })
        
    


         