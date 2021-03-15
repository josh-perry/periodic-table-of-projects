<template>
  <div class="periodic-table">
    <ElementSquare class="element-h" :element="Elements['Hydrogen']" />
    <ElementSquare class="element-he" :element="Elements['Helium']" />
    <ElementSquare :element="Elements['Lithium']" />
    <ElementSquare :element="Elements['Beryllium']" />
    <ElementSquare class="element-b" :element="Elements['Boron']" />
    <ElementSquare :element="Elements['Carbon']" />
    <ElementSquare :element="Elements['Nitrogen']" />
    <ElementSquare :element="Elements['Oxygen']" />
    <ElementSquare :element="Elements['Fluorine']" />
    <ElementSquare :element="Elements['Neon']" />

    <ElementSquare :element="Elements['Sodium']" />
    <ElementSquare :element="Elements['Magnesium']" />
    <ElementSquare class="element-al" :element="Elements['Aluminum']" />
    <ElementSquare :element="Elements['Silicon']" />
    <ElementSquare :element="Elements['Phosphorus']" />
    <ElementSquare :element="Elements['Sulfur']" />
    <ElementSquare :element="Elements['Chlorine']" />
    <ElementSquare :element="Elements['Argon']" />

    <ElementSquare :element="Elements['Potassium']" />
    <ElementSquare :element="Elements['Calcium']" />
    <ElementSquare :element="Elements['Scandium']" />
    <ElementSquare :element="Elements['Titanium']" />
    <ElementSquare :element="Elements['Vanadium']" />
    <ElementSquare :element="Elements['Chromium']" />
    <ElementSquare :element="Elements['Manganese']" />
    <ElementSquare :element="Elements['Iron']" />
    <ElementSquare :element="Elements['Cobalt']" />
    <ElementSquare :element="Elements['Nickel']" />
    <ElementSquare :element="Elements['Copper']" />
    <ElementSquare :element="Elements['Zinc']" />
    <ElementSquare :element="Elements['Gallium']" />
    <ElementSquare :element="Elements['Germanium']" />
    <ElementSquare :element="Elements['Arsenic']" />
    <ElementSquare :element="Elements['Selenium']" />
    <ElementSquare :element="Elements['Bromine']" />
    <ElementSquare :element="Elements['Krypton']" />

    <ElementSquare :element="Elements['Rubidium']" />
    <ElementSquare :element="Elements['Strontium']" />
    <ElementSquare :element="Elements['Yttrium']" />
    <ElementSquare :element="Elements['Zirconium']" />
    <ElementSquare :element="Elements['Niobium']" />
    <ElementSquare :element="Elements['Molybdenum']" />
    <ElementSquare :element="Elements['Technetium']" />
    <ElementSquare :element="Elements['Ruthenium']" />
    <ElementSquare :element="Elements['Rhodium']" />
    <ElementSquare :element="Elements['Palladium']" />
    <ElementSquare :element="Elements['Silver']" />
    <ElementSquare :element="Elements['Cadmium']" />
    <ElementSquare :element="Elements['Indium']" />
    <ElementSquare :element="Elements['Tin']" />
    <ElementSquare :element="Elements['Antimony']" />
    <ElementSquare :element="Elements['Tellurium']" />
    <ElementSquare :element="Elements['Iodine']" />
    <ElementSquare :element="Elements['Xenon']" />

    <ElementSquare :element="Elements['Cesium']" />
    <ElementSquare :element="Elements['Barium']" />
    <ElementSquare :element="Elements['Lanthanum']" />
    <ElementSquare :element="Elements['Hafnium']" />
    <ElementSquare :element="Elements['Tantalum']" />
    <ElementSquare :element="Elements['Tungsten']" />
    <ElementSquare :element="Elements['Rhenium']" />
    <ElementSquare :element="Elements['Osmium']" />
    <ElementSquare :element="Elements['Iridium']" />
    <ElementSquare :element="Elements['Platinum']" />
    <ElementSquare :element="Elements['Gold']" />
    <ElementSquare :element="Elements['Mercury']" />
    <ElementSquare :element="Elements['Thallium']" />
    <ElementSquare :element="Elements['Lead']" />
    <ElementSquare :element="Elements['Bismuth']" />
    <ElementSquare :element="Elements['Polonium']" />
    <ElementSquare :element="Elements['Astatine']" />
    <ElementSquare :element="Elements['Radon']" />

    <ElementSquare :element="Elements['Francium']" />
    <ElementSquare :element="Elements['Radium']" />
    <ElementSquare :element="Elements['Actinium']" />

    <ElementSquare :element="Elements['Rutherfordium']" />
    <ElementSquare :element="Elements['Dubnium']" />
    <ElementSquare :element="Elements['Seaborgium']" />
    <ElementSquare :element="Elements['Bohrium']" />
    <ElementSquare :element="Elements['Hassium']" />
    <ElementSquare :element="Elements['Meitnerium']" />
    <ElementSquare :element="Elements['Darmstadtium']" />
    <ElementSquare :element="Elements['Roentgenium']" />
    <ElementSquare :element="Elements['Copernicium']" />
    <ElementSquare :element="Elements['Nihonium']" />
    <ElementSquare :element="Elements['Flerovium']" />
    <ElementSquare :element="Elements['Moscovium']" />
    <ElementSquare :element="Elements['Livermorium']" />
    <ElementSquare :element="Elements['Tennessine']" />
    <ElementSquare :element="Elements['Oganesson']" />

    <ElementSquare class="element-la" :element="Elements['Lanthanum']" />
    <ElementSquare class="element-ce" :element="Elements['Cerium']" />
    <ElementSquare class="element-pr" :element="Elements['Praseodymium']" />
    <ElementSquare class="element-nd" :element="Elements['Neodymium']" />
    <ElementSquare class="element-pm" :element="Elements['Promethium']" />
    <ElementSquare class="element-sm" :element="Elements['Samarium']" />
    <ElementSquare class="element-eu" :element="Elements['Europium']" />
    <ElementSquare class="element-gd" :element="Elements['Gadolinium']" />
    <ElementSquare class="element-tb" :element="Elements['Terbium']" />
    <ElementSquare class="element-dy" :element="Elements['Dysprosium']" />
    <ElementSquare class="element-ho" :element="Elements['Holmium']" />
    <ElementSquare class="element-er" :element="Elements['Erbium']" />
    <ElementSquare class="element-tm" :element="Elements['Thulium']" />
    <ElementSquare class="element-yb" :element="Elements['Ytterbium']" />
    <ElementSquare class="element-lu" :element="Elements['Lutetium']" />

    <ElementSquare class="element-ac" :element="Elements['Actinium']" />
    <ElementSquare class="element-th" :element="Elements['Thorium']" />
    <ElementSquare class="element-pa" :element="Elements['Protactinium']" />
    <ElementSquare class="element-u" :element="Elements['Uranium']" />
    <ElementSquare class="element-np" :element="Elements['Neptunium']" />
    <ElementSquare class="element-pu" :element="Elements['Plutonium']" />
    <ElementSquare class="element-am" :element="Elements['Americium']" />
    <ElementSquare class="element-cm" :element="Elements['Curium']" />
    <ElementSquare class="element-bk" :element="Elements['Berkelium']" />
    <ElementSquare class="element-cf" :element="Elements['Californium']" />
    <ElementSquare class="element-es" :element="Elements['Einsteinium']" />
    <ElementSquare class="element-fm" :element="Elements['Fermium']" />
    <ElementSquare class="element-md" :element="Elements['Mendelevium']" />
    <ElementSquare class="element-no" :element="Elements['Nobelium']" />
    <ElementSquare class="element-lr" :element="Elements['Lawrencium']" />
  </div>
</template>

<script>
import Elements from '../static/json/meta.json'
import ElementSquare from './ElementSquare.vue'
import BlankElementSquare from './BlankElementSquare.vue'

export default {
  name: 'PeriodicTable',
  data ({ $http }) {
    return {
      Elements
    }
  }
}
</script>

<style scoped>
.periodic-table {
  display: grid;

  grid-template-columns: repeat(18, 1fr);
  grid-template-rows: repeat(10, 1fr);
  grid-gap: 4px;
  margin: 30px;
}

.element-al,
.element-b {
  grid-column-start: 13;
}

.element-he {
  grid-column-start: 18;
}

.element-ce,
.element-pr,
.element-nd,
.element-pm,
.element-sm,
.element-eu,
.element-gd,
.element-tb,
.element-dy,
.element-ho,
.element-er,
.element-tm,
.element-yb,
.element-lu,
.element-la {
  grid-row-start: 9;
}

.element-ac,
.element-th,
.element-pa,
.element-u,
.element-np,
.element-pu,
.element-am,
.element-cm,
.element-bk,
.element-cf,
.element-es,
.element-fm,
.element-md,
.element-no,
.element-lr {
  grid-row-start: 10;
}

.element-la,
.element-ac {
  grid-column-start: 3;
}

.element-ce,
.element-th {
  grid-column-start: 4;
}

.element-pr,
.element-pa {
  grid-column-start: 5;
}

.element-nd,
.element-u {
  grid-column-start: 6;
}

.element-pm,
.element-np {
  grid-column-start: 7;
}

.element-sm,
.element-pu {
  grid-column-start: 8;
}

.element-eu,
.element-am {
  grid-column-start: 9;
}

.element-gd,
.element-cm {
  grid-column-start: 10;
}

.element-tb,
.element-bk {
  grid-column-start: 11;
}

.element-dy,
.element-cf {
  grid-column-start: 12;
}

.element-ho,
.element-es {
  grid-column-start: 13;
}

.element-er,
.element-fm {
  grid-column-start: 14;
}

.element-tm,
.element-md {
  grid-column-start: 15;
}

.element-yb,
.element-no {
  grid-column-start: 16;
}

.element-lu,
.element-lr {
  grid-column-start: 17;
}

.element-square {
  width: 100%;
  height: 100%;
}
</style>
