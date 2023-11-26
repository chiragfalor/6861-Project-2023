/**
WebPPL code on tug of war world model
 **/

var lazyEffortPrior = 0.25
var normalEffortPrior = 0.5 
var extraEffortPrior = 0.25
var lazyPulling = 0.5
var normalPulling = 1
var extraPulling = 1.5

var strengthSD = 5
var strengthDistribution = Gaussian({mu: 50, sigma: strengthSD})

var tugOfWarModel = function() {

    var strength = mem(function(person) {
        var a = sample(strengthDistribution)
        return a
    })

    var effort = mem(function(person, match) {
        return categorical({
            ps: [lazyEffortPrior, normalEffortPrior, extraEffortPrior],
            vs: [lazyPulling, normalPulling, extraPulling]
        })
    })

    var pulling = function(person, match) {
        return (match == -1) ? categorical({
                ps: [lazyEffortPrior, normalEffortPrior, extraEffortPrior],
                vs: [lazyPulling, normalPulling, extraPulling]
            }) * strength(person) :
            effort(person, match) * strength(person)
    }

    var totalPulling = function(team, match) {
        return sum(map(function(person) {
            return pulling(person, match)
        }, team))
    }

    var deltaTeamStrength = function(team1, team2, match) {
        return totalPulling(team1, match) - totalPulling(team2, match)
    }

    var winner = function(team1, team2, match) {
        return deltaTeamStrength(team1, team2, match) > 0 ? 1 : 2
    }

}

var dist = Infer({
    method: 'rejection',
    samples: 1,
    model: tugOfWarModel
})