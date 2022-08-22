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

<style>
    h1 {
        padding-bottom: 50px;
    }

    ul {
        padding-top: 10px;
    }

    body {
        padding-bottom: 100px;
        text-align: left;
    }

    body a {
        font-weight: bolder;
    }

    h3 {
        padding-top: 30px;
        padding-bottom: 10px;
    }

    th {
        text-shadow: 0 0 5px;
    }

</style>

<main>
    <Navbar/>

    <h1 class="white text-center">
        Portfolio
    </h1>
    <div class="container">
    <body class="aqua">
        I love programming and robotics. I started with Scratch and LEGO MindStorms in middle school, and I have a diverse set of technologies under my belt at the present. <br><br>
        I'm proficient in:
        <ul>
            <li>Programming Languages like <term>Python</term> and <term>SQL</term>,</li>
            <li>Relational Databases like <term>PostgreSQL, MySQL</term> and <term>SQLite</term></li>
            <li> NoSQL Databases like <term>MongoDB</term></li>
            <li>Web Frameworks like <term>Svelte, Django, Flask, Sanic</term> and <term>FastAPI</term></li>
            <li>Version Control with <term>git</term></li>
            <li>Dependency Management and Packaging with <term>pip</term> and <term>poetry</term></li>
        </ul>

        I'm currently learning <term>Rust</term> to write high-performance code in places where Python won't do the trick.
        <br><br>
        <h3 class="glow">
            Achievements
        </h3>

        <table class="table">
            <thead>
                <tr>
                    {#each head as h}
                    <th scope="col">{h}</th>
                    {/each}
                </tr>
            </thead>
            <tbody>
                {#each awards as award}
                <tr>
                    <th>
                        <a class="clean pink-shine" href={award[1]}>{award[0]}</a>
                    </th>
                    {#each award.slice(2, award.length) as row}
                    <td>{row}</td>
                    {/each}
                </tr>
                {/each}
            </tbody>
        </table>

        <h3 class="glow">
            Projects
        </h3>
        You can check out my favorite projects <a href='/projects' class='pink-shine clean'>here</a>. <br>
        Also check out my GitHub: <a href="https://github.com/zeffo" class="pink-shine clean">github.com/zeffo</a>

    </body>
    </div> 
</main>