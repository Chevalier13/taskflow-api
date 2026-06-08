const { Router } = require('express');
const taskController = require('../controllers/taskController');

const router = Router();

router.get('/tasks', taskController.getAll);
router.post('/tasks', taskController.create);
router.put('/tasks/:id', taskController.update);
router.delete('/tasks/:id', taskController.delete);

module.exports = router;