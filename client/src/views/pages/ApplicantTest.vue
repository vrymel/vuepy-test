<template>
  <div>
    <div>
      <h3>Banned</h3>
      <div>
        <CButton block color="info">Canada</CButton>
        <CButton block color="info">Germany</CButton>
      </div>
      <span>Select Banned Countries</span>
    </div>

    <div>
      <CTabs variant="pills" :active-tab="1">
        <CTab title="Home">
          1. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
          et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
          officia deserunt mollit anim id est laborum.
        </CTab>
        <CTab title="Profile">
          2. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
          et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
          officia deserunt mollit anim id est laborum.
        </CTab>
      </CTabs>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ApplicantTest'
}
</script>
