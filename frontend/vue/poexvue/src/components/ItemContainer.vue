<template>
    <div :class="item_class + item.inventoryId" @mouseover="upHere = true" @mouseleave="upHere = false">
        <div class="itemIcon">
            <img :src="item.icon" alt="">
        </div>
    </div>
    <div v-show="upHere" class="ItemInfo">
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
    props: ['item'],
    data(){
        return {
            upHere: false,
            item_class: "ItemContainer "
        }
    }
}
</script>
<style>
    .itemIcon {
        max-width: fit-content;
        max-height: fit-content;
    }
    .ItemContainer {
        max-width: min-content;
        max-height: min-content;
        margin: 0px;
        position: absolute;
    }
    .ItemInfo {
        background-color: burlywood;
        z-index: 99;
    }
</style>