<template>
  <CContainer>
    <h2>Banned Countries</h2>

    <div>
      <p>Banned</p>
      <div class="d-flex">
        <CButton
            v-for="country in selectedCountries"
            :key="country"
            class="mr-2"
            color="info">
          {{ country }}
        </CButton>
      </div>
    </div>

    <div class="mt-5">
      <p>Select Banned Countries</p>
      <CTabs variant="pills" :active-tab="0">
        <CTab title="ABC">
          <CInputCheckbox label="Germany" @update:checked="addCountry('Germany', $event)"/>
          <CInputCheckbox label="Philippines" @update:checked="addCountry('Philippines', $event)"/>
        </CTab>
      </CTabs>
    </div>
  </CContainer>
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
