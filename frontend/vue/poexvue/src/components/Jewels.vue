<template>
    <div class="jewels">
        <item-container v-for="jewel in items" :item="jewel"/>
    </div>
</template>
<script>
import ItemContainer from '@/components/ItemContainer.vue'
export default {
    components: {ItemContainer},
    props: ['items'],
}
</script>
<style>
    .jewels {
        display: flex;
        flex-wrap: wrap;
    }
    .jewels .ItemContainer {
        position: relative;
    }
</style>