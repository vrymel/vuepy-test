<template>
  <div>
    <div>
      <h3>Banned</h3>
      <div>
        <CButton
            v-for="country in selectedCountries"
            :key="country"
            block
            color="info">
          {{ country }}
        </CButton>
      </div>
      <span>Select Banned Countries</span>
    </div>

    <div>
      <CTabs variant="pills" :active-tab="0">
        <CTab title="ABC">
          <CInputCheckbox label="Germany" @update:checked="addCountry('Germany', $event)" />
          <CInputCheckbox label="Philippines" @update:checked="addCountry('Philippines', $event)" />
        </CTab>
      </CTabs>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ApplicantTest',
  data() {
    return {
      selectedCountries: []
    }
  },
  methods: {
    addCountry(country, checked) {
      if (checked)
        this.selectedCountries.push(country);
      else
        this.selectedCountries = this.selectedCountries.filter((c) => c !== country)
    }
  }
}
</script>
