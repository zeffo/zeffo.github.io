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
			<h1 class="title">
				Hi! I'm Aman.
			</h1>
			<p style="padding-top:60px;">
				I ❤️ automation, concurrent programming and Star Wars. <br>
				You can find me on <a href="https://discord.com/users/325616103143505932" class="link"> Discord </a> 
				and <a href="https://github.com/zeffo" class="link"> GitHub</a>.
			</p>
		</body>
	</div>
</main>