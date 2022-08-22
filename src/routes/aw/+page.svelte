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
    .container {
        padding-right: 20px;
        padding-left: 20px;
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

<h1 class="white text-center">
    Animal Welfare
</h1>

<div class="container justify-content-center">
    <body class="text-center aqua">
        I'm very fond of animals, and I've rescued, rehabilitated and rehomed over 30 animals since 2015. <br>
        I regularly volunteer with local animal rescue NGOs, and I'm an ethical vegan. 
    </body>
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