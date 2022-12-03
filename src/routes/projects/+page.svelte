<script>
    import Navbar from "../../components/Navbar.svelte";
    // Title, URL, Description, Image URL
    let assets = 'projects/'
    let proj = [
        ['HK', 'https://github.com/zeffo/HK', 'A multipurpose discord bot', assets+'hk.jpg'],
        ['AmbiLight', 'https://youtu.be/_VMQRKT320A', 'System to synchronize monitor colors with a ARGB strip in real time', assets+'ambience.png'],
        ['zeffo.me', '/', 'My website, made with svelte and bootstrap', 'favicon.png'],
        ['Periodico', 'https://www.youtube.com/watch?v=BfJffhaNUBo', 'Robot to help newspaper vendors cut down on delivery times', assets+'periodico.png'],
        ['pytemplate', 'https://github.com/zeffo/pytemplate', 'pytemplate is a multithreaded CLI for rendering DocX templates.', assets+'pytemplate.png']
    ]
</script>

<Navbar />
<h1 class="title text-center">
    Projects
</h1>

<body>
    <div class="container-fluid no-collision">
        <div class="row g-1 justify-content-center" style="padding-top: 30px;">
            {#each proj as project}   
                <div class="card">
                    <a href={project[1]} class="clean" target="_blank" rel="noreferrer">
                        <h2 class="card-title text-center">
                            <a href={project[1]} class="link">{project[0]}</a>
                        </h2>
                        <p class="card-text">
                            {project[2]}
                        </p>
                    </a>
                </div>  
            {/each}
        </div>
    </div>
</body>