odoo.define('bike_rental.frontend', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.BikeRentalWidget = publicWidget.Widget.extend({
        selector: '#rental-form',
        events: {
            'submit': '_onSubmit',
        },

        start: function () {
            this._super.apply(this, arguments);
            this._initCalendar();
        },

        _onSubmit: function (ev) {
            var $form = $(ev.currentTarget);
            var duration = $form.find('#duration').val();
            var startDate = $form.find('#start_date').val();
            if (duration < 1) {
                ev.preventDefault();
                alert('Duration must be at least 1 day.');
            }
            if (new Date(startDate) < new Date()) {
                ev.preventDefault();
                alert('Start date cannot be in the past.');
            }
        },

        _initCalendar: function () {
            var calendarEl = document.getElementById('calendar');
            if (calendarEl) {
                var calendar = new FullCalendar.Calendar(calendarEl, {
                    initialView: 'dayGridMonth',
                    events: '/bikes/availability',
                });
                calendar.render();
            }
        },
    });

    return publicWidget.registry.BikeRentalWidget;
});