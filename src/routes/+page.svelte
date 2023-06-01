<script lang="ts">
  let news: any[] = [];
  for (let i = 0; i <= 10; i++) {
    news.push({
      page_url:
        "https://dtf.ru/games/1841059-cikly-lyubov-i-cikly-lyubvi-slozhnye-syuzhety-bayonetta",
      image_url:
        "https://leonardo.osnova.io/7adf51c4-05c1-5ad6-b405-6aabbef1f4bf/-/preview/1800/-/format/webp/",
      title: "Циклы, любовь и циклы любви — сложные сюжеты Bayonetta",
      description:
        "Что, если я скажу вам, что каждая Bayonetta была игрой о любви? Что, если за эталонным слешером и сложным сюжетом стоят несколько историй любви, переплетающихся воедино? Не верите? Ну что ж, обо всём по порядку.",
      viewers: 1000,
      likes: 250,
    });
  }
</script>

<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <p class="navbar-brand">HackGames</p>
    <form class="d-flex" role="search">
      <input
        class="form-control me-2"
        type="search"
        placeholder="Поиск"
        aria-label="Поиск"
      />
      <button class="btn btn-outline-success" type="submit"
        ><i class="bi bi-search" /></button
      >
    </form>
  </div>
</nav>

<div class="container">
  <div class="row justify-content-center">
    {#each news as element}
      <div class="col-lg-4 col-md-6 col-sm-12 mb-3">
        <div class="card shadow">
          <img src={element.image_url} class="card-img-top" alt="Header" />
          <div class="card-body">
            <h5 class="card-title">{element.title}</h5>
            {#if element.description}
              <p class="card-text">
                {element.description}
              </p>
            {/if}
            <a href={element.page_url} class="btn w-100 btn-primary">Читать</a>
          </div>
          <div class="card-footer">
            <i class="bi bi-eye" />
            {element.viewers}

            <i class="bi bi-heart" />
            {element.likes}
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
