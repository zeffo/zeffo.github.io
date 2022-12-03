<script>
    let pages = [
        ['home', '/'],
        ['projects', '/projects'],
        ['portfolio', '/portfolio'],
        ['animal welfare', '/aw'],
        
    ]
    import { page } from '$app/stores';
    let url = $page.url.pathname;

</script>

<style>


</style>

<nav class="navbar navbar-expand-sm navbar-dark static-top">
    <div class="container-fluid" id="navbar">
        <button data-bs-toggle="collapse" class="btn navbar-toggler shadow-none" data-bs-target="#navbarNav" style="margin-bottom:20px;">
            <span class="visually-hidden">Toggle navigation</span>
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav" style="font-size: 25px;text-align:left;">
            <ul class="navbar-nav mx-auto">
                {#each pages as page}
                <li class="nav-item px-3" class:current="{url===page[1]}">
                    <a class="nav-link" href={page[1]}>
                        {page[0]}
                    </a>
                </li>
                {/each}
            </ul>
        </div>
    </div>
</nav>