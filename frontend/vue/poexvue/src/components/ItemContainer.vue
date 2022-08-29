<template>
<div class="item">
    <div :class="item_class + item.inventoryId +' x'+ item.x" @mouseover="upHere = true" @mouseleave="upHere = false">
        <div class="itemIcon">
            <img :src="item.icon" alt="">
        </div>
    </div>
</div>
</template>
<script>
export default {
    props: ['item'],
    data(){
        return {
            upHere: false,
            item_class: "ItemContainer ",
            item_info_class: "ItemInfo ",
            item_class_prefix: "Info"
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
        
        width: max-content;
        text-align: center;
        /* inset: calc(100% * -2) 100px auto 0px; */
        /* transform: translate(0px, -10%); */
    }
    .item .ItemInfo {
        /* visibility: hidden; */
        position: absolute;
        transform: translate(0px, -50%);
    }
</style>