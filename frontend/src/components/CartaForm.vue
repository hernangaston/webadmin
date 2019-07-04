<template>
  <b-form enctype="multipart/form-data" @submit.prevent="$emit('processCarta', carta)">
    <b-row class="mt-3">
      <b-col sm="3">
        <b-form-group>
          <date-picker
            v-model="carta.fecha"
            :lang="lang"
            format="YYYY-MM-DD"
            :state="! $v.carta.fecha.$invalid"
            placeholder="FECHA"
            @input="$v.carta.$touch"
          ></date-picker>
        </b-form-group>
      </b-col>
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.numero"
            :state="! $v.carta.numero.$invalid"
            placeholder="Nro. CP"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback
            if="cartaInfo"
            v-if="$v.carta.$dirty"
          >Este campo es requerido y debe ser mayor a 4 caracteres</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.ctg"
            :state="! $v.carta.ctg.$invalid"
            placeholder="CTG"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback
            if="cartaInfo"
            v-if="$v.carta.$dirty"
          >Este campo es requerido y debe ser mayor a 8 caracteres</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.renspa"
            :state="! $v.carta.renspa.$invalid"
            placeholder="RENSPA"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback
            if="cartaInfo"
            v-if="$v.carta.$dirty"
          >Este campo es requerido y debe ser mayor a 8 caracteres</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Intermediario:
          <strong>{{ carta.intermediario }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.intermediario" :options="optionsinterm" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Rem. Comerc:
          <strong>{{ carta.remitente_comercial }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.remitente_comercial" :options="optionsrc" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Corr. comprador:
          <strong>{{ carta.corredor_comprador }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.corredor_comprador" :options="optionscorredor" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          MAT:
          <strong>{{ carta.mercado_a_termino }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.mercado_a_termino" :options="optionsmat" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Corr. Vendedor:
          <strong>{{ carta.corredor_vendedor }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.corredor_vendedor" :options="optionscorredor" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Entregador:
          <strong>{{ carta.entregador }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.entregador" :options="optionsentregador" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Destinatario:
          <strong>{{ carta.destinatario }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.destinatario" :options="optionsdestinatario" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Destino:
          <strong>{{ carta.destino }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.destino" :options="optionsdestino" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Intermediario Flete:
          <strong>{{ carta.interm_flete }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.interm_flete" :options="optionsinterm_flete" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Transportista:
          <strong>{{ carta.transportista }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select
          v-model="carta.transportista"
          :options="optionstransportista"
          @change="changeTrans()"
          class="mb-1"
        >
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="2">
        <div class="mb-1">
          Chofer:
          <strong>{{ carta.chofer }}</strong>
        </div>
      </b-col>
      <b-col sm="10">
        <b-form-select v-model="carta.chofer" :options="optionschofer" class="mb-1">
          <option :value="null" disabled>-- Please select an option --</option>
        </b-form-select>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.grano"
            :state="! $v.carta.grano.$invalid"
            placeholder="Grano/Especie"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback if="cartaInfo" v-if="$v.carta.$dirty">Este campo es requerido</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.tipo"
            :state="! $v.carta.tipo.$invalid"
            placeholder="Tipo"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback if="cartaInfo" v-if="$v.carta.$dirty">Este campo es requerido</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.cosecha"
            :state="! $v.carta.cosecha.$invalid"
            placeholder="Cosecha"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback if="cartaInfo" v-if="$v.carta.$dirty">Este campo es requerido</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
      <b-col sm="3">
        <b-form-group>
          <b-form-input
            autocomplete="off"
            id="carta"
            v-model="carta.contrato"
            :state="! $v.carta.contrato.$invalid"
            placeholder="contrato"
            @input="$v.carta.$touch"
          ></b-form-input>
          <b-form-invalid-feedback if="cartaInfo" v-if="$v.carta.$dirty">Este campo es requerido</b-form-invalid-feedback>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="3">
        <b-form-checkbox
          id="checkbox3"
          name="checkbox3"
          v-model="carta.pesada_en_destino"
          value="true"
          unchecked-value="false"
        >Pesada en destino</b-form-checkbox>
        <b-form-checkbox
          id="checkbox4"
          name="checkbox4"
          v-model="carta.kgs_estimados"
          value="true"
          unchecked-value="false"
        >Kgs. Estimados</b-form-checkbox>
        <b-form-invalid-feedback if="cartaInfo" v-if="$v.carta.$dirty">Este campo es requerido</b-form-invalid-feedback>
      </b-col>
      <b-col sm="3">
        <b-form-checkbox
          id="checkbox0"
          name="checkbox0"
          v-model="carta.declaracion_calidad"
          value="true"
          unchecked-value="false"
        >Declaracion de calidad</b-form-checkbox>
        <b-form-checkbox
          id="checkbox1"
          name="checkbox1"
          v-model="carta.conforme"
          value="true"
          unchecked-value="false"
        >Conforme</b-form-checkbox>
        <b-form-checkbox
          id="checkbox2"
          name="checkbox2"
          v-model="carta.condicional"
          value="true"
          unchecked-value="false"
        >Condicional</b-form-checkbox>
      </b-col>
      <b-col sm="3">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="peso_bruto"
          v-model="carta.peso_bruto"
          :state="! $v.carta.peso_bruto.$invalid"
          placeholder="Bruto"
          @input="$v.carta.$touch"
        ></b-form-input>
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="peso_tara"
          v-model="carta.peso_tara"
          :state="! $v.carta.peso_tara.$invalid"
          placeholder="Tara"
          @input="$v.carta.$touch"
        ></b-form-input>
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="peso_neto"
          v-model="carta.peso_neto"
          :state="! $v.carta.peso_neto.$invalid"
          placeholder="Neto"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
      <b-col sm="3">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="observaciones"
          v-model="carta.observaciones"
          :state="! $v.carta.observaciones.$invalid"
          placeholder="Observaciones"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="8">
        <h5>PROCEDENCIA DE LA MERCADERIA</h5>
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="direccion_procedencia"
          v-model="carta.direccion_procedencia"
          :state="! $v.carta.direccion_procedencia.$invalid"
          placeholder="Direccion de procedencia"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
      <b-col sm="4">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="establecimiento"
          v-model="carta.establecimiento"
          :state="! $v.carta.establecimiento.$invalid"
          placeholder="Establecimiento"
          @input="$v.carta.$touch"
        ></b-form-input>
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="localidad_procedencia"
          v-model="carta.localidad_procedencia"
          :state="! $v.carta.localidad_procedencia.$invalid"
          placeholder="Localidad"
          @input="$v.carta.$touch"
        ></b-form-input>
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="provincia_procedencia"
          v-model="carta.provincia_procedencia"
          :state="! $v.carta.provincia_procedencia.$invalid"
          placeholder="Provincia"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="3">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="kilometros"
          v-model="carta.kilometros"
          :state="! $v.carta.kilometros.$invalid"
          placeholder="Kilometros"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
      <b-col sm="3">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="tarifa"
          v-model="carta.tarifa"
          :state="! $v.carta.tarifa.$invalid"
          placeholder="Tarifa"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
      <b-col sm="3">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="declaracion_juarada_nombre"
          v-model="carta.declaracion_juarada_nombre"
          :state="! $v.carta.declaracion_juarada_nombre.$invalid"
          placeholder="Nombre y apellido"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
      <b-col sm="3">
        <b-form-input
          class="mb-1"
          autocomplete="off"
          id="declaracion_juarada_dni"
          v-model="carta.declaracion_juarada_dni"
          :state="! $v.carta.declaracion_juarada_dni.$invalid"
          placeholder="DNI"
          @input="$v.carta.$touch"
        ></b-form-input>
      </b-col>
    </b-row>
    <b-row class="mt-3 mb-3">
      <b-col sm="6">
        <input type="file" ref="fileInput" @change="selectedFile" />
      </b-col>
      <b-col>
        <div>Selected file: {{ carta.docfile ? carta.docfile.name : '' }}</div>
      </b-col>
      <b-col>
        <button @click="uploadFile">Submit file</button>
      </b-col>
    </b-row>

    <b-row class="mb-5">
      <b-button type="submit" variant="primary" :disabled="$v.carta.$invalid">{{ cartaSubmit }}</b-button>
    </b-row>
  </b-form>
</template>
<script>
import DatePicker from 'vue2-datepicker'
import { validationMixin } from 'vuelidate'
import { required, minLength } from 'vuelidate/lib/validators'
import Vue from 'vue'

import Cookies from 'js-cookie'

export default {
  components: { DatePicker },
  mixins: [validationMixin],
  props: {
    carta: {
      type: Object,
      required: true
    },
    cartaSubmit: {
      type: String,
      default: 'Crear CP'
    }
  },
  data () {
    return {
      lang: 'es',
      type: 'date',
      optionsinterm: [{ value: null, text: 'Please select an option' }],
      optionsrc: [{ value: null, text: 'Please select an option' }],
      optionscorredor: [{ value: null, text: 'Please select an option' }],
      optionsmat: [{ value: null, text: 'Please select an option' }],
      optionsentregador: [{ value: null, text: 'Please select an option' }],
      optionsdestinatario: [{ value: null, text: 'Please select an option' }],
      optionsdestino: [{ value: null, text: 'Please select an option' }],
      optionsinterm_flete: [{ value: null, text: 'Please select an option' }],
      optionstransportista: [{ value: null, text: 'Please select an option' }],
      optionschofer: [{ value: null, text: 'Please select an option' }],
      fileSelected: null
    }
  },
  beforeMount () {
    this.fetchIntermediarios()
    this.fetchRemitenteComercial()
    this.fetchCorredor()
    this.fetchMat()
    this.fetchEntregador()
    this.fetchDestinatario()
    this.fetchDestino()
    this.fetchIntermediarioFlete()
    this.fetchTransportista()
  },
  methods: {
    selectedFile () {
      this.fileSelected = this.$refs.fileInput.files[0]
      this.carta.docfile = this.$refs.fileInput.files[0]
      console.log(this.fileSelected.name)
    },
    uploadFile () {
      event.preventDefault()
      var csrftoken = Cookies.get('csrftoken')
      var data = new FormData()
      data.append('file', this.fileSelected)
      Vue.axios({
        method: 'PUT',
        url: 'cp/fileupload/' + this.fileSelected.name,
        headers: {
          'X-CSRFToken': csrftoken
        },
        data
      }).then(res => {
        return res.data
      })
    },
    async fetchIntermediarios () {
      const response = await Vue.axios({
        url: '/intermediarios/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsinterm.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchRemitenteComercial () {
      const response = await Vue.axios({
        url: '/rem_comercial/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsrc.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchCorredor () {
      const response = await Vue.axios({
        url: '/corredor/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionscorredor.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchMat () {
      const response = await Vue.axios({
        url: '/mat/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsmat.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchEntregador () {
      const response = await Vue.axios({
        url: '/entregador/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsentregador.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchDestinatario () {
      const response = await Vue.axios({
        url: '/destinatario/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsdestinatario.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchDestino () {
      const response = await Vue.axios({
        url: '/destino/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsdestino.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchIntermediarioFlete () {
      const response = await Vue.axios({
        url: '/intermediarioflete/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionsinterm_flete.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchTransportista () {
      const response = await Vue.axios({
        url: '/transportista/api/list/'
      })

      for (var i = response.data.length - 1; i >= 0; i--) {
        this.optionstransportista.push({
          value: response.data[i].id,
          text: response.data[i].nombre
        })
      }
    },
    async fetchChofer () {
      let response = await Vue.axios({
        url: '/chofer/api/list/'
      })
      return response
    },
    async changeTrans () {
      this.optionschofer = []
      let response = await this.fetchChofer()
      var res = []
      if (response) {
        res = response.data.filter(
          data => data.transportista === this.carta.transportista
        )
        for (var i = res.length - 1; i >= 0; i--) {
          this.optionschofer.push({
            value: res[i].id,
            text: res[i].apellido + ', ' + res[i].nombre
          })
        }
      }
    }
  },
  validations: {
    // a partir de aca tenemos acceso a this.$v que representa vuelidate
    carta: {
      numero: {
        required,
        minLength: minLength(4)
      },
      ctg: {
        required,
        minLength: minLength(8)
      },
      renspa: {
        minLength: minLength(8)
      },
      fecha: {
        required
      },
      grano: {
        required
      },
      tipo: {
        minLength: minLength(8)
      },
      cosecha: {
        required
      },
      contrato: {
        minLength: minLength(4)
      },
      peso_bruto: {
        required
      },
      peso_tara: {
        required
      },
      peso_neto: {
        required
      },
      observaciones: {
        minLength: minLength(8)
      },
      direccion_procedencia: {
        required
      },
      establecimiento: {
        minLength: minLength(4)
      },
      localidad_procedencia: {
        required
      },
      provincia_procedencia: {
        required
      },
      kilometros: {
        required
      },
      tarifa: {
        required
      },
      declaracion_juarada_nombre: {
        required
      },
      declaracion_juarada_dni: {
        required
      }
    }
  }
}
</script>
