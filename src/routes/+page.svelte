<script lang="ts">
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

  let news: Element[] = [];
  let filter: string = "";

  fetch(
    "https://raw.githubusercontent.com/igorechek06/Coddy2023/master/news.json"
  )
    .then((response) => response.json())
    .then((json) => (news = json));
</script>

<nav class="navbar bg-body-tertiary mb-3 sticky-top shadow-lg">
  <div class="container-fluid">
    <h1 class="navbar-brand">HackGames</h1>
    <div class="d-flex">
      <input
        class="form-control me-2"
        type="search"
        placeholder="Поиск"
        aria-label="Поиск"
        bind:value={filter}
      />
    </div>
  </div>
</nav>

<div class="container">
  <div class="row justify-content-center">
    {#each news as element}
      {#if element.title
        .toLowerCase()
        .includes(filter.toLowerCase()) || (element.description && element.description
            .toLowerCase()
            .includes(filter.toLowerCase())) || element.site_name
          .toLowerCase()
          .includes(filter.toLowerCase())}
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-12 mb-3">
          <div class="card shadow h-100">
            <img src={element.image_url} class="card-img-top" alt="Header" />
            <div class="card-body">
              <h5 class="card-title">{element.title}</h5>
              {#if element.description}
                <div class="overflow-auto" style="max-height: 10rem;">
                  <p class="card-text">
                    {element.description}
                  </p>
                </div>
              {/if}
              <a href={element.page_url}>Читать далее ...</a>
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
      {/if}
    {/each}
  </div>
</div>
