<!-- App.svelte -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  const API_BASE_URL = "http://localhost:80";

  let accessToken = null;
  let playlistId = "";
  let isDownloading = false;
  let errorMessage = "";

  async function authenticate() {
    const { data } = await axios.get(API_BASE_URL + "/auth");
    window.location.replace(data.url);
  }

  async function generateCharts() {
    if (isDownloading) return;
    isDownloading = true;
    errorMessage = "";

    const regex = /https:\/\/open\.spotify\.com\/playlist\/\w+/;
    if (!regex.test(playlistId)) {
      errorMessage = "Invalid playlist link format";
      isDownloading = false;
      return;
    }

    try {
      const parts = playlistId.split("/");
      playlistId = parts[parts.length - 1];
      const { data } = await axios.post(
        API_BASE_URL + "/download",
        {
          accessToken,
          playlistId,
        },
        {
          responseType: "blob", 
        }
      );

      const zipBlob = new Blob([data], { type: "application/zip" });
      const zipUrl = URL.createObjectURL(zipBlob);
      const link = document.createElement("a");
      link.href = zipUrl;
      link.download = "GeneratedCharts.zip";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(zipUrl);
      authenticate();
      console.log(`Downloaded playlist: ${playlistId}`);
    } catch (error) {
      console.error(error);
    } finally {
      isDownloading = false;
    }
  }

  onMount(() => {
    const params = new URLSearchParams(window.location.search);
    accessToken = params.get("code");
  });
</script>

<main>
  <h1>Clone Hero Chart Generator</h1>
  {#if !accessToken}
    <button on:click={authenticate}>Authenticate with Spotify</button>
  {:else}
    <div>
      <input type="text" placeholder="Playlist Link" bind:value={playlistId} />
      <p style="color: red">{errorMessage}</p>
      <button on:click={generateCharts} disabled={isDownloading}>
        {#if isDownloading}
          Downloading...
        {:else}
          Generate
        {/if}
      </button>
    </div>
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }
  h1 {
    color: #ff3e00;
    /* color: blue; */
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }
  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
