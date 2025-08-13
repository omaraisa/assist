"""
Example usage of the new multi-field statistics system
This shows how to integrate the new functions with your existing Chart.js frontend
"""

# Example 1: Generate data for a single widget
def get_widget_data_for_frontend(layer_name, widget_id):
    """
    Function to call from your web API to get Chart.js data for a specific widget
    """
    from app.spatial_functions import SpatialFunctions
    
    spatial_func = SpatialFunctions()
    result = spatial_func.generate_widget_chart_data(layer_name, widget_id=widget_id)
    
    if result.get("success"):
        # Return the Chart.js configuration
        return {
            "success": True,
            "chartConfig": {
                "type": result["chart_type"],
                "data": result["data"],
                "options": result["options"]
            },
            "statistics": result.get("statistics", {}),
            "widget_info": result.get("widget_info", {})
        }
    else:
        return {"success": False, "error": result.get("error")}

# Example 2: Generate data for custom field combination
def get_custom_chart_data(layer_name, fields, chart_type):
    """
    Function to generate chart data for custom field combinations (AI-generated charts)
    """
    from app.spatial_functions import SpatialFunctions
    
    spatial_func = SpatialFunctions()
    result = spatial_func.generate_multi_field_statistics(layer_name, fields, chart_type)
    
    if result.get("success"):
        return {
            "success": True,
            "chartConfig": {
                "type": result["chart_type"],
                "data": result["data"],
                "options": result["options"]
            },
            "statistics": result.get("statistics", {})
        }
    else:
        return {"success": False, "error": result.get("error")}

# Example 3: Generate all dashboard data at once
def refresh_entire_dashboard(layer_name):
    """
    Function to regenerate all chart data for the dashboard
    """
    from app.spatial_functions import SpatialFunctions
    
    spatial_func = SpatialFunctions()
    result = spatial_func.generate_all_dashboard_data(layer_name)
    
    if result.get("success"):
        # Transform for frontend use
        frontend_data = {}
        for widget_id, widget_data in result["widget_data"].items():
            frontend_data[widget_id] = {
                "type": widget_data["chart_type"],
                "data": widget_data["data"],
                "options": widget_data["options"],
                "statistics": widget_data.get("statistics", {})
            }
        
        return {
            "success": True,
            "widgets": frontend_data,
            "layout": result["dashboard_layout"],
            "summary": {
                "total_widgets": result["total_widgets"],
                "successful_widgets": result["successful_widgets"],
                "errors": result.get("errors", [])
            }
        }
    else:
        return {"success": False, "error": result.get("error")}

# Example 4: Flask/FastAPI endpoint examples
"""
# Flask example
@app.route('/api/dashboard/widget/<widget_id>/data')
def get_widget_chart_data(widget_id):
    layer_name = request.args.get('layer', 'default_layer')
    result = get_widget_data_for_frontend(layer_name, widget_id)
    return jsonify(result)

@app.route('/api/dashboard/custom-chart', methods=['POST'])
def create_custom_chart():
    data = request.json
    layer_name = data.get('layer')
    fields = data.get('fields')
    chart_type = data.get('chart_type')
    
    result = get_custom_chart_data(layer_name, fields, chart_type)
    return jsonify(result)

@app.route('/api/dashboard/refresh')
def refresh_dashboard():
    layer_name = request.args.get('layer', 'default_layer')
    result = refresh_entire_dashboard(layer_name)
    return jsonify(result)
"""

# Example 5: JavaScript frontend usage
"""
// JavaScript example for using the generated data

// Function to update a single chart
async function updateWidget(widgetId, layerName) {
    try {
        const response = await fetch(`/api/dashboard/widget/${widgetId}/data?layer=${layerName}`);
        const result = await response.json();
        
        if (result.success) {
            // Create or update Chart.js chart
            const chartElement = document.getElementById(`chart-${widgetId}`);
            new Chart(chartElement, result.chartConfig);
        } else {
            console.error('Failed to load widget data:', result.error);
        }
    } catch (error) {
        console.error('Error updating widget:', error);
    }
}

// Function to create custom AI-generated chart
async function createCustomChart(fields, chartType, layerName) {
    try {
        const response = await fetch('/api/dashboard/custom-chart', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                fields: fields,
                chart_type: chartType,
                layer: layerName
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Create new chart with AI-generated configuration
            const newChartElement = document.createElement('canvas');
            document.getElementById('charts-container').appendChild(newChartElement);
            new Chart(newChartElement, result.chartConfig);
        } else {
            console.error('Failed to create custom chart:', result.error);
        }
    } catch (error) {
        console.error('Error creating custom chart:', error);
    }
}

// Function to refresh entire dashboard
async function refreshDashboard(layerName) {
    try {
        const response = await fetch(`/api/dashboard/refresh?layer=${layerName}`);
        const result = await response.json();
        
        if (result.success) {
            // Update all widgets
            Object.entries(result.widgets).forEach(([widgetId, chartConfig]) => {
                const chartElement = document.getElementById(`chart-${widgetId}`);
                if (chartElement) {
                    // Destroy existing chart if it exists
                    if (Chart.getChart(chartElement)) {
                        Chart.getChart(chartElement).destroy();
                    }
                    // Create new chart
                    new Chart(chartElement, {
                        type: chartConfig.type,
                        data: chartConfig.data,
                        options: chartConfig.options
                    });
                }
            });
        } else {
            console.error('Failed to refresh dashboard:', result.error);
        }
    } catch (error) {
        console.error('Error refreshing dashboard:', error);
    }
}
"""

print("Multi-field statistics integration examples loaded!")
print("Key functions available:")
print("1. get_widget_data_for_frontend() - Single widget data")
print("2. get_custom_chart_data() - AI-generated chart data") 
print("3. refresh_entire_dashboard() - Complete dashboard refresh")
print()
print("Chart types supported:")
print("- scatter: 2 numeric fields correlation")
print("- bar/column: categorical + numeric OR categorical counts")
print("- pie: single categorical field")
print("- histogram: single numeric field distribution")
print("- line: time series or multi-field trends")
