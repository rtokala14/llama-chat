<script lang="ts">
    import {QueryClient, QueryClientProvider} from "@tanstack/svelte-query";
    import {browser} from "$app/environment";
    import {SvelteQueryDevtools} from "@tanstack/svelte-query-devtools";

    let {children} = $props();

    const queryClient = new QueryClient({
        defaultOptions: {
            queries: {
                enabled: browser
            }
        }
    });
</script>

<QueryClientProvider client={queryClient}>
    <main>
        {@render children()}
    </main>

    <SvelteQueryDevtools />
</QueryClientProvider>