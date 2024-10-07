<script lang="ts">
    import {createQuery} from "@tanstack/svelte-query";

    const query = createQuery({
        queryKey: ['hello'],
        queryFn: async () => ((await fetch('http://localhost:5000/hello')).json()),
    })

</script>

<h1>Welcome to SvelteKit</h1>
<div>
    {#if $query.isLoading}
        <p>Loading...</p>
    {:else if $query.isError}
        <p>Error: {$query.error.message}</p>
    {:else if $query.isSuccess}
        <p>Success: {$query.data.message}</p>
    {/if}
</div>