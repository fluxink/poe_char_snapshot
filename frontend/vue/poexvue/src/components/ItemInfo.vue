<template>
    <div class="item-info">
        <h3>{{item.name}}</h3>
        <h3>{{item.typeLine}}</h3>
        <br v-if="item.implicitMods">
        <p v-for="mode in item.implicitMods">{{mode}}</p>
        <br v-if="item.implicitMods">
        <p v-for="mode in item.explicitMods">{{mode}}</p>
    </div>
</template>
<script>
export default {
    props: ['item']
}
</script>
<style>
    .item-info {
        grid-column-start: 1;
        grid-row-start: 3;
    }
</style>