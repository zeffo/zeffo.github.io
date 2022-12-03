<script>
    import Navbar from "../../components/Navbar.svelte";
    let head = ["Name", "Description"]
    let path = "certs/"
    let awards = [
        ["IIT-B TechFest International Robowars", path+"robowars.png", "An international robot combat competition hosted by IIT Bombay for TechFest. 3rd Place - 2020"],
        ["YLAC High School Achievers", path+"ylac.jpg", "A highly selective program that provides a platform for students to gain diverse perspectives and develop leadership skills to create long-lasting impact"],
        ["PY4E 5 Course Specialization", path+"py4e.pdf", "An in-depth python course offered by the University of Michigan via Coursera"],
        ["KPIT vSolve Robotics Competition", '', "An interschool robotics competition. 1st place - 2018, 2nd place - 2019"],
        ["Youngistaani Innovator's Conclave", path+"youngistaani.jpg", "An interschool conclave where select students were able to showcase their innovations and get feedback from industry leaders"]
    ]
</script>

<Navbar />

<h1 class="title text-center">
    Portfolio
</h1>

<body>
    <div class="container-fluid no-collision">
    </div>
</body>