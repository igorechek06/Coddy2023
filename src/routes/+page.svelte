<script lang="ts" context="module">
  type Element = {
    page_url: string;
    image_url: string;
    title: string;
    description: string | null;
    viewers: number;
    likes: number;
    site_name: string;
    site_link: string;
  };

  let response = await fetch(
    "https://raw.githubusercontent.com/igorechek06/Coddy2023/master/news.json"
  );
  let news: Element[] = await response.json();
</script>

<nav class="navbar bg-body-tertiary mb-3 sticky-top shadow-lg">
  <div class="container-fluid">
    <h1 class="navbar-brand">HackGames</h1>
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
      <div class="col-xl-3 col-lg-4 col-md-6 col-sm-12 mb-3">
        <div class="card shadow h-100">
          <img src={element.image_url} class="card-img-top" alt="Header" />
          <div class="card-body">
            <h5 class="card-title">{element.title}</h5>
            {#if element.description}
              <div class="overflow-auto">
                <p class="card-text">
                  {element.description}
                </p>
              </div>
            {/if}
            <a href={element.page_url} class="btn w-100 btn-primary">Читать</a>
          </div>
          <div class="card-footer justify-content-between d-flex">
            <div>
              <i class="bi bi-eye" />
              {element.viewers}
            </div>
            <div>
              <a href={element.site_link} class="link-secondary">
                <i class="bi bi-box-arrow-up-left" />
                {element.site_name}
              </a>
            </div>
            <div>
              <i class="bi bi-heart" />
              {element.likes}
            </div>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
