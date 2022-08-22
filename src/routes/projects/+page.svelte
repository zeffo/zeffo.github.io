<script>
    import Navbar from "../../components/Navbar.svelte";

    // Title, URL, Description, Image URL
    let assets = 'projects/'
    let proj = [
        ['HK', 'https://github.com/zeffo/HK', 'A multipurpose discord bot', assets+'hk.jpg'],
        ['AmbiLight', 'https://youtu.be/_VMQRKT320A', 'System to synchronize monitor colors with a ARGB strip in real time', assets+'ambience.png'],
        ['zeffo.me', '/', 'My website, made with svelte and bootstrap', 'favicon.png'],
        ['Periodico', 'https://www.youtube.com/watch?v=BfJffhaNUBo', 'A newspaper sequencing robot to help newspaper vendors cut down on delivery times', assets+'periodico.png'],
        ['pytemplate', 'https://github.com/zeffo/pytemplate', 'pytemplate is a multithreaded CLI for rendering DocX templates.', assets+'pytemplate.png']
    ]
</script>

<style>

    .card {
        background-color: #0c0c11;
        max-width: 475px;
        margin: 30px;
    }

    .card a {
        font-weight: bold;
    }

    .card img {
        max-height: 150px;
    }

    .card:hover {
        transform: scale(1.05);
    }

    .container-fluid {
        padding-top: 30px;
        margin-bottom: 50px;
        padding-bottom: 50px;
        text-align: left;
    }


</style>

<Navbar/>

<h1 class="white text-center">
    Projects
</h1>

<body>
    <div class="container-fluid">
        <div class="row g-0 justify-content-center">
            {#each proj as project}
                <div class="card">
                    <div class="row g-0">
                        <div class="col my-auto">
                            <img src={project[3]} class="img-fluid rounded-start" alt={project[0]}/> 
                        </div>
                        <div class="col-sm-8">
                            <div class="card-body">
                                <h5 class="card-title">
                                    <a href={project[1]} class="clean pink-shine">{project[0]}</a>
                                </h5>
                                <p class="card-text">
                                    {project[2]}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    </div>
</body>


