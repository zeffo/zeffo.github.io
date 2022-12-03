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
    let tech = [
        ["Programming Languages", ["Python3", "Rust", "JS"]],
        ["Technologies", ["Postgres", "Svelte", "Git", "Django", "Vim", "Arch"]],
    ]
</script>

<Navbar />

<h1 class="title text-center">
    Portfolio
</h1>

<body>
    <div class="portfolio container no-collision text-center">
        {#each tech as row}
            <h5>
                {row[0]}
            </h5>
            <div class="row justify-content-center">
                {#each row[1] as t}
                    <div class="col" style="max-width: 150px;">
                        <img src="icons/{t}.svg" alt={t} class="icon">
                        {t}
                    </div>
                {/each}
            </div>
            <br>
        {/each}
        <h5>
            Achievements
        </h5>
        <table class="table">
            <thead>
                <tr>     
                    <th scope="col" class="table-name">Name</th>
                    <th scope="col" class="table-desc">Description</th>
                </tr>
            </thead>
            <tbody>
                {#each awards as award}
                <tr>
                    <th>
                        <a class="link" href={award[1]}>{award[0]}</a>
                    </th>
                    {#each award.slice(2, award.length) as row}
                    <td>{row}</td>
                    {/each}
                </tr>
                {/each}
            </tbody>
        </table>
    </div>
</body>