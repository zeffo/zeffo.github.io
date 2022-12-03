<script>
    import Navbar from "../../components/Navbar.svelte";
    let path = 'animals/'
    let images = 24;
    let initial = path+'main.jpg'
</script>

<Navbar/>

<style>
    h1 {
        padding-bottom: 30px;
    }
    .carousel {
        max-height: 500px;
        padding-bottom: 100px;
    }
    @media(min-width:990px) {
        body {
            margin-bottom: 50px;
        }
    }
    .carousel > .carousel-inner > .carousel-item > img {
        margin: 0 auto;
        display: block;
        height: 500px;
        object-fit: contain;
        padding-bottom: 50px;
    }
    .carousel-control-next, .carousel-control-prev {
        padding-bottom: 50px;
    }
</style>

<h1 class="title text-center">
    Rescues
</h1>

<body>
    <p class="text-center">
        Here are some of the animals I've helped rescue and rehome:
    </p>
    <div class="container-fluid justify-content-center no-collision">
        <div class="container-fluid">
            <div id="carousel" class="carousel slide mx-auto" data-bs-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src={initial} class="img-fluid mx-auto" alt='Probably a cat'>
                    </div>
                    {#each Array(images) as _, index(index)}
                    <div class="carousel-item">
                        <img src={path+index+".jpg"} class="img-fluid mx-auto" alt="Probably a cat">
                    </div>
                    {/each}
                </div>

                <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next" data-bs-interval="5000">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>
    </div>
</body> 