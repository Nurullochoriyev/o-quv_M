from django.shortcuts import render
from .models import *
def Studentlar(request):
    new=Student.objects.all()
    new2 = Curs.objects.all()
    data={
        "dc": new2,
        "db":new,
        "title":"student"
    }
    return render(request,'news/stu.html',context=data)










def Curslar(request):
    new2=Curs.objects.all()
    data2={
        "dc":new2,
        "title":"curslar"
    }
    return render(request,'news/cur.html',context=data2)







#
#
# <nav class="navbar navbar-expand-lg navbar-light bg-light">
#   <div class="container-fluid">
#     <a class="navbar-brand" href="#">Navbar</a>
#     <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#       <span class="navbar-toggler-icon"></span>
#     </button>
#     <div class="collapse navbar-collapse" id="navbarSupportedContent">
#       <ul class="navbar-nav me-auto mb-2 mb-lg-0">
#         <li class="nav-item">
#           <a class="nav-link active" aria-current="page" href="#">Home</a>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link" href="#">Link</a>
#         </li>
#         <li class="nav-item dropdown">
#           <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
#             Dropdown
#           </a>
#           <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
#             <li><a class="dropdown-item" href="#">Action</a></li>
#             <li><a class="dropdown-item" href="#">Another action</a></li>
#             <li><hr class="dropdown-divider"></li>
#             <li><a class="dropdown-item" href="#">Something else here</a></li>
#           </ul>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
#         </li>
#       </ul>
#       <form class="d-flex">
#         <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
#         <button class="btn btn-outline-success" type="submit">Search</button>
#       </form>
#     </div>
#   </div>
# </nav>
#
#
# <div class="card text-center">
#   <div class="card-header">
#     Featured
#   </div>
#   <div class="card-body">
#     <h5 class="card-title">Special title treatment</h5>
#     <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
#     <a href="#" class="btn btn-primary">Go somewhere</a>
#   </div>
#   <div class="card-footer text-muted">
#     2 days ago
#   </div>
# </div>
# {% for item in dc %}
# <div class="container">
#         <div class="row">
#             <div class="col-6 bg-primary text-white p-3">
#                 Birinchi ma'lumot
#             </div>
#             <div class="col-6 bg-success text-white p-3">
#                 Ikkinchi ma'lumot
#
#
#
# <div class="card text-center">
#   <div class="card-header">
#       {{item.title}}
# <!--    Featured-->
#   </div>
#   <div class="card-body">
#     <h5 class="card-title">{{item.start_time}}</h5>
#     <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
#     <a href="#" class="btn btn-primary">Go somewhere</a>
#   </div>
#   <div class="card-footer text-muted">
#       {{item.end_time}}
# <!--    2 days ago-->
#   </div>
# </div>
#
# {% endfor %}
#
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
# <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
#
