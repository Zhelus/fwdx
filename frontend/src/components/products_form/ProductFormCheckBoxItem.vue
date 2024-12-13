<script setup>
import { ref, watch } from 'vue';

// Props
const props = defineProps(['sectionHeader', 'optionsList', 'selectionVar']);
const emit = defineEmits(['update:selectionVar']); // Emit event for v-model

// Internal state to track checkbox selections
const localSelectionVar = ref([...props.selectionVar]);

// Watch for changes in local state and emit updates to parent
watch(localSelectionVar, (newValue) => {
  emit('update:selectionVar', newValue);
});
</script>

<template>
  <div class="checkbox-item-container">
    <h3 class="section-header">{{ sectionHeader }}</h3>
    <div class="checkboxes-container">
      <div v-for="(option, index) in optionsList" :key="index" class="checkbox-wrapper">
        <input
          class="form-checkbox"
          type="checkbox"
          :value="option.value"
          v-model="localSelectionVar"
          :id="'checkbox-' + index"
        />
        <label class="checkbox-label" :for="'checkbox-' + index">{{ option.name }}</label>
      </div>
    </div>
  </div>
</template>

<style scoped>
.checkbox-item-container {
  display: flex;
  flex-direction: column;
  height: auto;
  width: 40%;
  min-width: 380px;
  background-color: transparent;
  margin-bottom: var(--form-element-spacing);
  margin-top: 0rem;
}

.checkboxes-container {
  display: flex;
  flex-wrap: wrap;
  height: auto;
  align-content: space-between;
  row-gap: var(--form-checkbox-row-gap);
}

.section-header {
  color: var(--dark-gray-text);
  font-size: var(--subheading-size);
  font-weight: var(--subheading-weight);
  line-height: var(--subheading-size);
  text-align: left;
  text-justify: top;
  margin-bottom: 0.25rem;
}

.checkbox-wrapper {
  width: 33%;
  height: 22%;
  min-height: var(--body-text-size);
  background-color: transparent;
  display: flex;
  justify-content: flex-start;
  align-items: flex-end;
  padding: 0;
}

.form-checkbox {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 1.5vh;
  width: 1.5vh;
  min-height: var(--body-text-size);
  min-width: var(--body-text-size);
  outline: 0;
  border: 1px solid var(--light-gray-outline);
  border-radius: 2px;
  background-color: var(--fwdx-white);
}

.form-checkbox:hover {
  cursor: pointer;
  border: 1px solid var(--fwdx-yellow);
}

.form-checkbox:checked {
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  appearance: checkbox;
  accent-color: var(--fwdx-yellow);
}

.checkbox-label {
  color: var(--dark-gray-text);
  margin-left: 0.25rem;
  font-size: var(--body-text-size);
  align-self: flex-end;
  line-height: 1em;
}
</style>
