<script>
	import Navbar from '../components/Navbar.svelte'
</script>

<style>
	@media(max-width:990px) {
		.container-fluid {
			padding-right: 20px;
			padding-left: 20px;
		}
	}
</style>

<Navbar/>

<main>
	<div class="container-fluid">
		<body class="text-center">
			<h1 class="white glow" style="padding-top:50px;">
				Hi! I'm Aman.
			</h1>
			<p class="lead aqua" style="padding-top:30px;">
				I ❤️ anything to do with automation, concurrency and Star Wars. <br>
				You can find me on <a href="https://discord.com/users/325616103143505932" class="clean pink-shine"> Discord </a> 
				and <a href="https://github.com/zeffo" class="clean pink-shine"> GitHub. </a>
			</p>
		</body>
	</div>
</main>