const data = require('./qoe_peak_non_peak.json')
//console.log(data)
const categoriesPeak = [];
const categoriesNonPeak = [];
const colors = {
	AMAZON: '#424242',
	AZURE: '#9E9E9E',
	GOOGLE: '#EEEEEE'
}
const providersPeak = {
	AMAZON: [],
	AZURE: [],
	GOOGLE: []
}
const providersNonPeak = {
	AMAZON: [],
	AZURE: [],
	GOOGLE: []
}

Object.keys(data).forEach(region => {
	Object.keys(data[region]).forEach(timeZone => {
		const categoryName = `${region}-${timeZone}`
		
		const peak_hours_qoe_map = {};
		const non_peak_hours_qoe_map = {}
		Object.keys(data[region][timeZone]).forEach(provider => {
			let peak_hours_qoe = data[region][timeZone][provider].peak_hours_qoe
			peak_hours_qoe =  Number(peak_hours_qoe.toFixed(2));
			peak_hours_qoe_map[provider] = peak_hours_qoe

			let non_peak_hours_qoe = data[region][timeZone][provider].non_peak_hours_qoe
			non_peak_hours_qoe =  Number(non_peak_hours_qoe.toFixed(2));
			non_peak_hours_qoe_map[provider] = non_peak_hours_qoe
			// providers[provider].push(peak_hours_qoe)
		})
		if(peak_hours_qoe_map.AMAZON === 0 && peak_hours_qoe_map.AZURE === 0 && peak_hours_qoe_map.GOOGLE === 0){
			return
		}
		
		Object.keys(peak_hours_qoe_map).forEach(e => providersPeak[e].push(peak_hours_qoe_map[e]))
		categoriesPeak.push(categoryName)

		if(non_peak_hours_qoe_map.AMAZON === 0 && non_peak_hours_qoe_map.AZURE === 0 && non_peak_hours_qoe_map.GOOGLE === 0){
			return
		}
		
		Object.keys(non_peak_hours_qoe_map).forEach(e => providersNonPeak[e].push(non_peak_hours_qoe_map[e]))
		categoriesNonPeak.push(categoryName)

	})
})

const result = {
	peak: {},
	nonPeak: {}
}

let series = []
Object.keys(providersPeak).forEach(provider => {
	series.push({
		name: provider,
		data: providersPeak[provider]
	})
})
result.peak.series = series
result.peak.categories = categoriesPeak

series =[];
Object.keys(providersNonPeak).forEach(provider => {
	series.push({
		name: provider,
		data: providersNonPeak[provider],
		color: colors[provider]
	})
})
result.nonPeak.series = series
result.nonPeak.categories = categoriesNonPeak

console.log('\n\n\n\n\n\n\n\n\n')
console.log(JSON.stringify(result))
